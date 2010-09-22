import os.path
from Globals import package_home
from StringIO import StringIO
from eea.epub.tests.base import EpubFunctionalTestCase

class ImporterTest(EpubFunctionalTestCase):

    def afterSetUp(self):
        self.setRoles(['Manager'])

        filePath = os.path.join(package_home(globals()), 'test2.epub')
        f = open(filePath)
        fileContent = StringIO(f.read())
        f.close()

        view = self.portal.restrictedTraverse('@@epub_import_view')
        view.importFile(fileContent)

        self.rootEpubFolder = getattr(self.portal, 'climate-change-impact-in-europe', None)

    def test_toc(self):
        view = self.rootEpubFolder.restrictedTraverse('@@epub_toc_logic')
        navPoints = view.getNavPoints()
        self.failUnless(len(navPoints) == 10)

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = makeSuite(ImporterTest)
    return  TestSuite(suite)
