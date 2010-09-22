from Products.Five import BrowserView
from zope.app.annotation.interfaces import IAnnotations

class EpubTocLogic(BrowserView):

    def getNavPoints(self):
        annotations = IAnnotations(self.context.getCanonical())
        mapping = annotations.get('eea.epub')
        return mapping['toc']
