from zope.interface import Interface

class IExportView(Interface):
    pass

class IImportView(Interface):
    pass

class IEpubTocLogic(Interface):

    def getNavPoints():
        pass

class IEpubUtils(Interface):

    def getEpubFormatURL():
        pass

    def getEbook():
        pass

    def isImportedEbook():
        pass

    def isImportedChapter():
        pass

    def isPartOfImportedBook():
        pass
