from zope import interface
from persistent import Persistent
from zope.component.factory import Factory
from sparc.event import IEvent
from sparc.event.event import SparcEvent

@interface.implementer(IEvent)
class PersistentSparcEvent(SparcEvent, Persistent):
    """A Sparc Entity that can be persisted in a ZODB"""
persistentSparcEventFactory = Factory(PersistentSparcEvent)