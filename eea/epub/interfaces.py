""" Marker Iterfaces for Epub
"""
from zope.interface import Interface

class IImportedBook(Interface):
    """ Marker interface for epub root folder """

class IImportedChapter(Interface):
    """ Marker interface for each imported chapter """

class IExportable(Interface):
    """ Marker interface for all epub exporable content types """

class IImportedImage(Interface):
    """ Marker interface for imported epub images """

# Browser layer
from eea.epub.browser.interfaces import ILayer

# Events
from eea.epub.events.interfaces import IEPUBEvent
from eea.epub.events.interfaces import IEPUBExportFail
from eea.epub.events.interfaces import IEPUBExportSuccess
from eea.epub.events.interfaces import IAsyncEPUBEvent
from eea.epub.events.interfaces import IAsyncEPUBExportFail
from eea.epub.events.interfaces import IAsyncEPUBExportSuccess

__all__ = [
    ILayer.__name__,
    IEPUBEvent.__name__,
    IEPUBExportFail.__name__,
    IEPUBExportSuccess.__name__,
    IAsyncEPUBEvent.__name__,
    IAsyncEPUBExportFail.__name__,
    IAsyncEPUBExportSuccess.__name__,
]
