from Acquisition import aq_base
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import utils
from eea.epub.interfaces import IImportedBook
from eea.epub.interfaces import IImportedChapter
from eea.epub.interfaces import IImportedImage

class EpubUtils(BrowserView):

    def getEbook(self):
        obj = self.context
        portal_url = getToolByName(obj, 'portal_url')	    
        portal = portal_url.getPortalObject()
        while not IImportedBook.providedBy(obj) and aq_base(obj) is not aq_base(portal):
            obj = utils.parent(obj)
        return obj

    def isImportedEbook(self):
        return IImportedBook.providedBy(self.context)

    def isImportedChapter(self):
        return IImportedChapter.providedBy(self.context)

    def isImportedImage(self):
        return IImportedImage.providedBy(self.context)
