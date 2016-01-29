from zope.component.factory import Factory
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty
from sparc.entity import SparcEntity
from interfaces import IAlert

class SparcAlert(SparcEntity):
    implements(IAlert)
    
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
        for event in self._events:
            yield event
sparcAlertFactory = Factory(SparcAlert)