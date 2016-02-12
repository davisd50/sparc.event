from sparc.i18n import SparcMessageFactory
MessageFactory = SparcMessageFactory('sparc.event')


# Configuration (this package only)
from importlib import import_module
from sparc.configuration.zcml import Configure as SparcConfigure
def Configure():
    SparcConfigure([import_module(__name__),
                    import_module('sparc.asset')])

from interfaces import IAlert
from interfaces import IAlerts
from interfaces import IEvent
from interfaces import IEvents

from event import SparcEvent
from alert import SparcAlert