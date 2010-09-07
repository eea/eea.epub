from zope.interface import Interface

class IExportView(Interface):
    pass

class IImportView(Interface):
    
    def getNumberOfImportedProducts():
        pass

    def hasImportResults():
        pass
