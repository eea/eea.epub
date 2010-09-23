from Acquisition import aq_base
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import utils
from eea.epub.interfaces import IImportedBook
from eea.epub.interfaces import IImportedChapter
from eea.epub.interfaces import IImportedImage
from eea.epub.interfaces import IExportable

class EpubUtils(BrowserView):

    def getEbook(self):
        obj = self.context
        portal_url = getToolByName(obj, 'portal_url')	    
        portal = portal_url.getPortalObject()
        while not IImportedBook.providedBy(obj) and aq_base(obj) is not aq_base(portal):
            obj = utils.parent(obj)
        return obj

    def isEpubExportable(self):
        return IExportable.providedBy(self.context)

    def isImportedEbook(self):
        return IImportedBook.providedBy(self.context)

    def isImportedChapter(self):
        return IImportedChapter.providedBy(self.context)

    def isImportedImage(self):
        return IImportedImage.providedBy(self.context)

    def isPartOfImportedBook(self):
        return self.isImportedEbook() or self.isImportedChapter() or self.isImportedImage()

    def getEpubFormatURL(self):
        if self.isPartOfImportedBook():
            ebook = self.getEbook()
            return ebook.absolute_url() + '/original.epub'
        elif self.isEpubExportable():
            return self.context.absolute_url() + '/epub_view'
        return ''
