from zope.interface import Interface

class IImportedBook(Interface):
    """ Marker interface for epub root folder """

class IImportedChapter(Interface):
    """ Marker interface for each imported chapter """
