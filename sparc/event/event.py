from zope.interface import implements
from sparc.entity import SparcEntity
from interfaces import IEvent

class SparcEvent(SparcEntity):
    implements(IEvent)
    
    def __init__(self, **kwargs):
        super(SparcEvent, self).__init__(**kwargs)
        self._entities = kwargs['entities'] if 'entities' in kwargs else []
        self.datetime = kwargs['datetime']
        self.url = kwargs['url'] if 'url' in kwargs else None

    def entities(self):
        for entity in self._entities:
            yield entity
