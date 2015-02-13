""" Sync events
"""

from zope.interface import implementer
from eea.epub.events.interfaces import IEPUBExportFail
from eea.epub.events.interfaces import IEPUBExportSuccess
from eea.epub.events import EPUBEvent

@implementer(IEPUBExportFail)
class EPUBExportFail(EPUBEvent):
    """ Event triggered when a ePub export job failed
    """

@implementer(IEPUBExportSuccess)
class EPUBExportSuccess(EPUBEvent):
    """ Event triggered when a ePub export job succeeded
    """
