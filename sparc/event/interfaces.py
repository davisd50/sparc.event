from zope import schema
from zope.interface import Interface
from sparc.entity import IEntity
from sparc.event import MessageFactory as _

class IEvent(IEntity):
    """A notable occurence that happened at a point in time"""
    def entities():
        """Returns iterable of IEntity objects related to event"""
    datetime = schema.Datetime(
            title = _(u'Occurance datetime'),
            description = _(u'The datetime of the event occurance'),
            required = True
            )

class IAlert(IEntity):
    """An alert"""
    def events():
        """Returns iterable of ordered IEvent objects related to alert"""
        
    datetime = schema.Datetime(
            title = _(u'Alert datetime'),
            description = _(u'The datetime of the alert'),
            required = True
            )
    severity = schema.Choice(
            title = _(u'Alert severity'),
            description = _(u'Severity is based on criticality and fidelity'),
            required = True,
            values=[u'informational',u'low',u'medium',u'high',u'critical']
            )
