from zope.app.annotation.interfaces import IAnnotations
from Acquisition import aq_base
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import utils
from eea.epub.interfaces import IImportedBook

class EpubTocLogic(BrowserView):

    def getNavPoints(self):
        # 1. find ebook
        obj = self.context
        portal_url = getToolByName(obj, 'portal_url')	    
        portal = portal_url.getPortalObject()
        while not IImportedBook.providedBy(obj) and aq_base(obj) is not aq_base(portal):
            obj = utils.parent(obj)

        # 2. extract toc
        annotations = IAnnotations(obj)
        mapping = annotations.get('eea.epub')
        return mapping['toc']
