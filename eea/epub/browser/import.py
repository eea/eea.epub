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

    @property
    def rootFilePath(self):
        fileContent = self.zipFile.read('META-INF/container.xml')
        xml = ET.XML(fileContent)
        xml = stripNamespaces(xml)
        xml = xml.find('rootfiles')
        xml = xml.find('rootfile')
        path = xml.get('full-path')
        return path

    @property
    def title(self):
        fileContent = self.zipFile.read(self.rootFilePath)
        xml = ET.XML(fileContent)
        xml = stripNamespaces(xml)
        xml = xml.find('metadata')
        xml = xml.find('title')
        title = xml.text
        return title

    @property
    def ploneID(self):
        return self.title.strip().lower().replace(' ', '-')

class ImportView(BrowserView):

    template = ViewPageTemplateFile('epub.pt')

    def importFile(self, epubFile):
        zipFile = ZipFile(epubFile, 'r')
        epub = EpubFile(zipFile)
        self.context.invokeFactory('Folder', id=epub.ploneID)
