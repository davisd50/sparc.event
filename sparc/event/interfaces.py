from zope import schema
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
            title = _(u'Broadcast datetime'),
            description = _(u'The datetime of the alert broadcast'),
            required = True
            )
    severity = schema.Choice(
            title = _(u'Alert severity'),
            description = _(u'Severity is based on criticality and fidelity'),
            required = True,
            values=[u'low',u'medium',u'high',u'critical']
            )
