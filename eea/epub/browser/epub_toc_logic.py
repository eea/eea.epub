from zope.app.annotation.interfaces import IAnnotations
from Products.Five import BrowserView

class EpubTocLogic(BrowserView):

    def getNavPoints(self):
        utils = self.context.restrictedTraverse('@@epub_utils')
        ebook = utils.getEbook()
        annotations = IAnnotations(ebook)
        mapping = annotations.get('eea.epub')
        return mapping['toc']
