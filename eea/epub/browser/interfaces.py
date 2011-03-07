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

    def getNavPoints(): #pyflakes, #pylint: disable-msg = E0211
        """ getNavPoints interface method
        """
        pass

class IEpubUtils(Interface):
    """ IEpubUtils interface
    """

    def getEpubFormatURL(): #pyflakes, #pylint: disable-msg = E0211
        """ getEpubFormatURL interface method
        """
        pass

    def getEbook(): #pyflakes, #pylint: disable-msg = E0211
        """ getEbook interface method
        """
        pass

    def isImportedEbook(): #pyflakes, #pylint: disable-msg = E0211
        """ isImportedEbook interface method
        """
        pass

    def isImportedChapter(): #pyflakes, #pylint: disable-msg = E0211
        """ isImportedChapter interface method
        """
        pass

    def isPartOfImportedBook(): #pyflakes, #pylint: disable-msg = E0211
        """ isPartOfImportedBook interface method
        """
        pass
