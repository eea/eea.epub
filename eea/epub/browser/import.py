from elementtree import ElementTree as ET
from zipfile import ZipFile
from zope.app.pagetemplate import ViewPageTemplateFile
from Products.Five import BrowserView
from zope.interface import alsoProvides
from eea.epub.interfaces import IImportedBook
from eea.epub.interfaces import IImportedChapter
from eea.epub.interfaces import IImportedImage

def titleToId(title):
    return title.strip().strip('!@#$%^&*()<>./+').lower().replace(' ', '-')

def elemTagWithoutNamespace(elem):
    """Remove the xmlns that ElementTree inserts before the tag name

    If a namespace is present, ElementTree prefixes the tag names in
    'Clark's Notation', e.g. {http://www.w3.org/2005/Atom}feed. To make it
    easier to select by tag, we remove this.

    http://stackoverflow.com/questions/1249876
    """
    assert not isinstance(elem, str), 'Make sure you pass in the element, not the tag'
    if '}' in elem.tag:
        return elem.tag.split('}')[1]
    return elem.tag

def stripNamespaces(node):
    node.tag = elemTagWithoutNamespace(node)
    for elem in node.getchildren():
        elem.tag = elemTagWithoutNamespace(elem)
        stripNamespaces(elem)
    return node

class EpubFile(object):
    
    def __init__(self, zipFile):
        self.zipFile = zipFile
        self.cache = {}

    @property
    def rootFile(self):
        if 'rootFile' in self.cache:
            return self.cache['rootFile']

        file = self.zipFile.read('META-INF/container.xml')
        xml = ET.XML(file)
        xml = stripNamespaces(xml)
        xml = xml.find('rootfiles')
        xml = xml.find('rootfile')
        rootFilePath = xml.get('full-path')

        fileContent = self.zipFile.read(rootFilePath)
        xml = ET.XML(fileContent)
        xml = stripNamespaces(xml)

        self.cache['rootFile'] = xml
        return xml

    @property
    def coverImageData(self):
        if 'coverImageData' in self.cache:
            return self.cache['coverImageData']

        for elem in self.rootFile.find('manifest').findall('item'):
            type = elem.get('media-type', '')
            name = elem.get('type', '')
            id = elem.get('id', '')
            if type.startswith('image') and (name.startswith('cover') or id.startswith('cover')):
                coverImageData = self.zipFile.read('OEBPS/' + elem.get('href'))
                self.cache['coverImageData'] = coverImageData
                return coverImageData

        return None
            
    @property
    def title(self):
        xml = self.rootFile
        xml = xml.find('metadata')
        xml = xml.find('title')
        return xml.text

    @property
    def chapters(self):
        guide = self.rootFile.find('guide')
        if guide == None:
            return []

        chapters = []
        for elem in guide.getchildren():
            if elem.get('type') == 'text':
                fileName = 'OEBPS/' + elem.get('href')
                fileContent = self.zipFile.read(fileName)
                html = ET.XML(fileContent)
                html = stripNamespaces(html)
                html = html.find('body')
                description = html.find('p')
                html.remove(description)
                description = description.text.strip()
                h1 = html.find('h1')
                if h1 != None:
                    html.remove(h1)
                html = ET.tostring(html)
                chapters.append({
                    'id': elem.get('href'),
                    'title': elem.get('title'),
                    'content': html,
                    'description': description,
                })
        return chapters

    @property
    def images(self):
        if not 'images' in self.cache:
            self.cache['images'] = []
            for elem in self.rootFile.find('manifest').getchildren():
                if elem.get('media-type').startswith('image'):
                    self.cache['images'].append({
                        'href': elem.get('href'),
                    })
        return self.cache['images']

    @property
    def creator(self):
        if not 'creator' in self.cache:
            elem = self.rootFile.find('metadata').find('creator')
            if elem != None:
                self.cache['creator'] = elem.text
            else:
                self.cache['creator'] = None
        return self.cache['creator']

    @property
    def language(self):
        elem = self.rootFile.find('metadata').find('language')
        if elem != None:
            return elem.text
        return None

    @property
    def ploneID(self):
        return titleToId(self.title)

class ImportView(BrowserView):

    template = ViewPageTemplateFile('epub_import_form.pt')

    def __call__(self):
        if self.request.environ['REQUEST_METHOD'] == 'GET':
            return self.template(self)
        elif self.request.environ['REQUEST_METHOD'] == 'POST':
            httpFileUpload = self.request.form.values()[0]
            self.count = self.importFile(httpFileUpload)
            return self.template(self)

    def getNumberOfImportedProducts(self):
        return getattr(self, 'count', 0)

    def hasImportResults(self):
        return hasattr(self, 'count')

    def importFile(self, epubFile):
        zipFile = ZipFile(epubFile, 'r')
        epub = EpubFile(zipFile)

        # Generate unique ID
        id = epub.ploneID
        count = 0
        while hasattr(self.context, id):
            count += 1
            id = '%s-%i' % (epub.ploneID, count)

        folder = self.context[self.context.invokeFactory('Folder', id=id)]
        folder.setTitle(epub.title)
        if epub.creator != None:
            folder.setCreators([epub.creator])
        alsoProvides(folder, IImportedBook) 
        folder.reindexObject()

        if epub.coverImageData != None:
            folder.invokeFactory('Image', id='epub_cover', image=epub.coverImageData)
        
        for image in epub.images:
            workingDirectory = folder
            urlParts = image['href'].split('/')
            for urlPart in urlParts:
                if urlPart == urlParts[-1]:
                    path = 'OEBPS/' + image['href']
                    data = epub.zipFile.read(path)
                    image = workingDirectory[workingDirectory.invokeFactory('Image', id=urlPart, image=data)]
                    alsoProvides(image, IImportedImage) 
                    image.reindexObject()
                elif not hasattr(workingDirectory, urlPart):
                    workingDirectory = workingDirectory[workingDirectory.invokeFactory('Folder', id=urlPart)]
                else:
                    workingDirectory = workingDirectory[urlPart]

        count = 0
        for chapter in epub.chapters:
            count += 1;
            article = folder[folder.invokeFactory('Article', id=chapter['id'])]
            article.setTitle(chapter['title'])
            article.setText(chapter['content'])
            article.setDescription(chapter['description'])
            alsoProvides(article, IImportedChapter) 
            article.reindexObject()
        return count
