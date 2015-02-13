""" Events
"""
from zope.interface import Interface
from zope.component.interfaces import IObjectEvent

class IEPUBEvent(IObjectEvent):
    """ Base Event Interface for all ePub events
    """

class IEPUBExportSuccess(IEPUBEvent):
    """ ePub export succeeded
    """

class IEPUBExportFail(IEPUBEvent):
    """ ePub export failed
    """

class IAsyncEPUBEvent(IEPUBEvent):
    """ Base Event Interface for all Async ePub events
    """

class IAsyncEPUBExportSuccess(IAsyncEPUBEvent):
    """ Async job for ePub export succeeded
    """

class IAsyncEPUBExportFail(IAsyncEPUBEvent):
    """ Async job for ePub export failed
    """

class IEPUBContextWrapper(Interface):
    """ Context wrapper used by async events
    """
