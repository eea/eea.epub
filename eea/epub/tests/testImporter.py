import os.path
from Globals import package_home
from StringIO import StringIO
from eea.pagedesign.tests.base import EEAMegaTestCase

class ImporterTest(EEAMegaTestCase):

    def afterSetUp(self):
        self.setRoles(['Manager'])

        filePath = os.path.join(package_home(globals()), 'test.epub')
        f = open(filePath)
        fileContent = StringIO(f.read())
        f.close()

        view = self.portal.restrictedTraverse('@@epub_import_view')
        view.importFile(fileContent)

    def test_folderStructure(self):
        rootEpubFolder = getattr(self.portal, 'from-urban-spaces-to-urban-ecosystems', None)
        self.failUnless(rootEpubFolder is not None)
        brains = rootEpubFolder.getFolderContents()
        self.failUnless(len(brains) == 1) # EPUB contained one chapter

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = makeSuite(ImporterTest)
    return  TestSuite(suite)
