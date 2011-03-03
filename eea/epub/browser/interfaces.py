""" Browser Interfaces
"""
from zope.interface import Interface

class IExportView(Interface):
    """ IExportView interface
    """
    pass

class IImportView(Interface):
    """ IImportView interface
    """
    pass

class IEpubTocLogic(Interface):
    """ IEpubTocLogic interface
    """

    def getNavPoints():
        """ getNavPoints interface method
        """
        pass

class IEpubUtils(Interface):
    """ IEpubUtils interface
    """

    def getEpubFormatURL():
        """ getEpubFormatURL interface method
        """
        pass

    def getEbook():
        """ getEbook interface method
        """
        pass

    def isImportedEbook():
        """ isImportedEbook interface method
        """
        pass

    def isImportedChapter():
        """ isImportedChapter interface method
        """
        pass

    def isPartOfImportedBook():
        """ isPartOfImportedBook interface method
        """
        pass
