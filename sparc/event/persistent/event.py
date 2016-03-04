from zope.interface import implements
from persistent import Persistent
from zope.component.factory import Factory
from sparc.event import IEvent
from sparc.event.event import SparcEvent

class PersistentSparcEvent(SparcEvent, Persistent):
    """A Sparc Entity that can be persisted in a ZODB"""
    implements(IEvent)
persistentSparcEventFactory = Factory(PersistentSparcEvent)