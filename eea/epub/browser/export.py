from Products.Five import BrowserView
from zope.pagetemplate.pagetemplatefile import PageTemplateFile
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from StringIO import StringIO
from zipfile import ZipFile

class ExportView(BrowserView):

    template = ViewPageTemplateFile('epub.pt')

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        self.request.response.setHeader('Content-Type', 'application/xml+epub')
        self.request.response.setHeader('Content-Disposition', 'attachment; filename=%s.epub' % self.context.id)
        template = self.template()
        output = StringIO()
        myzip = ZipFile(output, 'w')
        myzip.writestr('mimetype', 'application/epub+zip')
        myzip.writestr('chapter1.xhtml', template)
        myzip.close()
        output.seek(0)
        return output.read()
