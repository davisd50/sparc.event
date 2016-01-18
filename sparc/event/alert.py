from zope.interface import implements
from sparc.entity import SparcEntity
from interfaces import IAlert
from interfaces import ISecurityAlert

class SparcAlert(SparcEntity):
    implements(IAlert)
    
    def __init__(self, **kwargs):
        super(SparcAlert, self).__init__(**kwargs)
        self._events = kwargs['events'] if 'events' in kwargs else []
        self.datetime = kwargs['datetime']
        self.severity = kwargs['severity']
        self.tags = kwargs['tags'] if 'tags' in kwargs else set()

    def events(self):
        for event in self._events:
            yield event

class SparcSecurityAlert(SparcAlert):
    implements(ISecurityAlert)