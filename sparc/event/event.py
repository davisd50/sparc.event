from zope.component.factory import Factory
from zope import interface
from zope.schema.fieldproperty import FieldProperty
from sparc.entity import SparcEntity
from .interfaces import IEvent

@interface.implementer(IEvent)
class SparcEvent(SparcEntity):
    
    def __init__(self, **kwargs):
        super(SparcEvent, self).__init__(**kwargs)
        self._entities = kwargs['entities'] if 'entities' in kwargs else set()
        self.datetime = kwargs['datetime']

    datetime = FieldProperty(IEvent['datetime'])

    def entities(self):
        return iter(self._entities) # pickle-safe
sparcEventFactory = Factory(SparcEvent)