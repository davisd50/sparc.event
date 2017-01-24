from zope.component.factory import Factory
from zope import interface
from zope.schema.fieldproperty import FieldProperty
from sparc.entity import SparcEntity
from .interfaces import IAlert

@interface.implementer(IAlert)
class SparcAlert(SparcEntity):
    
    def __init__(self, **kwargs):
        super(SparcAlert, self).__init__(**kwargs)
        self._events = kwargs['events'] if 'events' in kwargs else []
        self.datetime = kwargs['datetime']
        self.severity = kwargs['severity']
        self.system = kwargs['system']

    datetime = FieldProperty(IAlert['datetime'])
    severity = FieldProperty(IAlert['severity'])
    system = FieldProperty(IAlert['system'])

    def events(self):
        return iter(self._events) #pickle safe
sparcAlertFactory = Factory(SparcAlert)