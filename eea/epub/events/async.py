""" Async events
"""

from zope.interface import implementer
from eea.epub.events.interfaces import IAsyncEPUBExportFail
from eea.epub.events.interfaces import IAsyncEPUBExportSuccess
from eea.epub.events import AsyncEPUBEvent

@implementer(IAsyncEPUBExportFail)
class AsyncEPUBExportFail(AsyncEPUBEvent):
    """ Event triggered when an async EPUB export job failed
    """

@implementer(IAsyncEPUBExportSuccess)
class AsyncEPUBExportSuccess(AsyncEPUBEvent):
    """ Event triggered when an async EPUB export job succeeded
    """
