import os.path
from Globals import package_home
from StringIO import StringIO
from eea.pagedesign.tests.base import EEAMegaTestCase
from eea.epub.interfaces import IImportedBook
from eea.epub.interfaces import IImportedChapter
from eea.epub.interfaces import IImportedImage

class ImporterTest(EEAMegaTestCase):

    def afterSetUp(self):
        self.setRoles(['Manager'])

        filePath = os.path.join(package_home(globals()), 'test.epub')
        f = open(filePath)
        fileContent = StringIO(f.read())
        f.close()

        view = self.portal.restrictedTraverse('@@epub_import_view')
        view.importFile(fileContent)

        self.rootEpubFolder = getattr(self.portal, 'climate-change-impact-in-europe', None)

    def test_folderStructure(self):
        self.failUnless(self.rootEpubFolder is not None)
        self.failUnless(IImportedBook.providedBy(self.rootEpubFolder))

        # There should be one imported chapter
        brains = self.rootEpubFolder.getFolderContents({'portal_type':'Article'})
        self.failUnless(len(brains) == 1) # EPUB contained one chapter

        chapter = brains[0]
        self.failUnless(IImportedChapter.providedBy(chapter.getObject()))
        self.failUnless(chapter['id'] == 'chapter1.xhtml')
        self.failUnless(chapter['Title'] == 'Text')

    def test_coverImage(self):
        self.failUnless(self.rootEpubFolder.epub_cover.portal_type == 'Image')

    def test_creator(self):
        self.failUnless(self.rootEpubFolder.Creator() == 'S\xc3\xb8ren Roug')

    def test_imagesImportedCorrectly(self):
        brains = self.rootEpubFolder['Pictures'].getFolderContents({'portal_type': 'Image'})
        self.failUnless(IImportedImage.providedBy(brains[0].getObject()))
        self.failUnless(len(brains) == 9)

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = makeSuite(ImporterTest)
    return  TestSuite(suite)
