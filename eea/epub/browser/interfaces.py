from zope.interface import Interface

class IExportView(Interface):
    pass

class IImportView(Interface):
    
    def getNumberOfImportedProducts():
        pass

    def hasImportResults():
        pass

class IEpubTocLogic(Interface):

    def getNavPoints():
        pass

class IEpubUtils(Interface):

    def getEbook():
        pass

    def isImportedEbook():
        pass

    def isImportedChapter():
        pass
