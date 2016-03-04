from zope.interface import implements
from persistent import Persistent
from zope.component.factory import Factory
from sparc.event import IAlert
from sparc.event.alert import SparcAlert

class PersistentSparcAlert(SparcAlert, Persistent):
    """A Sparc Entity that can be persisted in a ZODB"""
    implements(IAlert)
persistentSparcAlertFactory = Factory(PersistentSparcAlert)