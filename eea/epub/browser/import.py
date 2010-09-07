from elementtree import ElementTree as ET
from zipfile import ZipFile
from zope.app.pagetemplate import ViewPageTemplateFile
from Products.Five import BrowserView

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
    def rootFilePath(self):
        fileContent = self.zipFile.read('META-INF/container.xml')
        xml = ET.XML(fileContent)
        xml = stripNamespaces(xml)
        xml = xml.find('rootfiles')
        xml = xml.find('rootfile')
        return xml.get('full-path')

    @property
    def rootFile(self):
        if 'rootFile' in self.cache:
            return self.cache['rootFile']
        fileContent = self.zipFile.read(self.rootFilePath)
        xml = ET.XML(fileContent)
        xml = stripNamespaces(xml)
        self.cache['rootFile'] = xml
        return xml

    @property
    def title(self):
        xml = self.rootFile
        xml = xml.find('metadata')
        xml = xml.find('title')
        return xml.text

    @property
    def chapterFiles(self):
        xml = self.rootFile
        xml = xml.find('manifest')
        chapters = []
        allowedContentTypes = [
            'application/xhtml+xml',
            'text/html',
        ]
        for elem in xml.getchildren():
            if elem.get('media-type') in allowedContentTypes:
                fileName = 'OEBPS/' + elem.get('href')
                chapters.append(fileName)
        return chapters

    @property
    def chapters(self):
        chapters = []
        for chapterFile in self.chapterFiles:
            content = self.zipFile.read(chapterFile)
            chapters.append(content)
        return chapters

    @property
    def ploneID(self):
        return self.title.strip().lower().replace(' ', '-')

class ImportView(BrowserView):

    template = ViewPageTemplateFile('epub_import_form.pt')

    def __call__(self):
        if self.request.environ['REQUEST_METHOD'] == 'GET':
            return self.template()
        elif self.request.environ['REQUEST_METHOD'] == 'POST':
            httpFileUpload = self.request.form.values()[0]
            epubFile = httpFileUpload.read()
            self.importFile(epubFile)

    def importFile(self, epubFile):
        zipFile = ZipFile(epubFile, 'r')
        epub = EpubFile(zipFile)
        folder = self.context[self.context.invokeFactory('Folder', id=epub.ploneID)]
        folder.setTitle(epub.title)
        count = 0
        for text in epub.chapters:
            count += 1;
            folder.invokeFactory('Article', id=str(count))
