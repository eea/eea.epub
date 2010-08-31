from StringIO import StringIO
from zipfile import ZipFile
from zope.app.pagetemplate import ViewPageTemplateFile
from Products.Five import BrowserView

class ExportView(BrowserView):

    template = ViewPageTemplateFile('epub.pt')

    def __call__(self):
        response = self.request.response
        response.setHeader('Content-Type', 'application/xml+epub')
        response.setHeader('Content-Disposition', 'attachment; filename=%s.epub' % self.context.id)

        templateOutput = self.template(self)
        templateOutput = templateOutput.decode('utf-8') # This encoding circus was required for including context.getText() in the template
        templateOutput = templateOutput.encode('utf-8')
        inMemoryOutputFile = StringIO()

        zipFile = ZipFile(inMemoryOutputFile, 'w')
        zipFile.writestr('mimetype', 'application/epub+zip')
        zipFile.writestr('chapter1.xhtml', templateOutput)
        zipFile.close()

        inMemoryOutputFile.seek(0)
        return inMemoryOutputFile.read()
