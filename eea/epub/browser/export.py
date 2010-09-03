import os.path
from StringIO import StringIO
from zipfile import ZipFile
from zope.app.pagetemplate import ViewPageTemplateFile
from Globals import package_home
from Products.Five import BrowserView

def replace(filePath, variables):
    filePath = os.path.join(package_home(globals()), 'static', filePath)
    f = open(filePath)
    content = f.read()
    f.close()
    content = content % variables
    return content

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

        variables = {
            'TITLE': self.context.Title(),
            'IDENTIFIER': self.context.absolute_url()
        }

        zipFile = ZipFile(inMemoryOutputFile, 'w')
        zipFile.writestr('mimetype', 'application/epub+zip')
        zipFile.writestr('META-INF/container.xml', replace('META-INF/container.xml', {}))

        zipFile.writestr('OEBPS/content.xhtml', templateOutput)
        zipFile.writestr('OEBPS/content.opf', replace('OEBPS/content.opf', variables))
        zipFile.writestr('OEBPS/toc.ncx', replace('OEBPS/toc.ncx', variables))
        zipFile.close()

        inMemoryOutputFile.seek(0)
        return inMemoryOutputFile.read()
