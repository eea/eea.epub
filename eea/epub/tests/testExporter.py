from zipfile import ZipFile
from StringIO import StringIO
from eea.pagedesign.tests.base import EEAMegaTestCase

class ExporterTest(EEAMegaTestCase):

    def afterSetUp(self):
        self.setRoles(['Manager'])
        self.article = self.portal[self.portal.invokeFactory('Article', id='testArticle')]
        self.article.setTitle('TestTitle')
        self.article.setText('TestText')

        context = self.article
        view = context.restrictedTraverse('@@epub_view')
        self.response = view.request.response
        self.responseOutput = view()

    def test_responseHeaders(self):
        self.failUnless(self.response.getHeader('Content-Type') == 'application/xml+epub')
        self.failUnless(self.response.getHeader('Content-Disposition') == 'attachment; filename=testArticle.epub')

    def test_zipFile(self):
        responseOutput = StringIO(self.responseOutput)
        zipFile = ZipFile(responseOutput, 'r')
        fileNames = zipFile.namelist()
        self.failUnless('mimetype' in fileNames)
        self.failUnless('OEBPS/content.xhtml' in fileNames)

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = makeSuite(ExporterTest)
    return  TestSuite(suite)
