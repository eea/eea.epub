""" Events
"""
from zope.interface import implementer
from eea.epub.events.interfaces import IEPUBEvent, IAsyncEPUBEvent

@implementer(IEPUBEvent)
class EPUBEvent(object):
    """ Abstract ePub event
    """
    def __init__(self, context, **kwargs):
        self.object = context

@implementer(IAsyncEPUBEvent)
class EPUBAsyncEvent(EPUBEvent):
    """ Abstract ePub event for all async ePub events
    """
