from zope import interface
from persistent import Persistent
from zope.component.factory import Factory
from sparc.event import IAlert
from sparc.event.alert import SparcAlert

@interface.implementer(IAlert)
class PersistentSparcAlert(SparcAlert, Persistent):
    """A Sparc Entity that can be persisted in a ZODB"""
persistentSparcAlertFactory = Factory(PersistentSparcAlert)