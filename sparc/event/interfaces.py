from zope import schema
from sparc.entity import IEntity
from sparc.entity import ITaggable


class IEvent(IEntity):
    """A notable occurence that happened at a point in time"""
    def entities():
        """Returns iterable of IEntity objects related to event"""
    datetime = schema.Datetime(
            title = u'Occurance datetime',
            description = u'The datetime of the event occurance',
            required = True
            )
    url = schema.TextLine(
            title=_(u"URL to query results with event"),
            description=(u"convenience pointer to external system hosting event data"),
            )

class IAlert(IEntity, ITaggable):
    """An alert"""
    def events():
        """Returns iterable of ordered IEvent objects related to alert"""
        
    datetime = schema.Datetime(
            title = u'Broadcast datetime',
            description = u'The datetime of the alert broadcast',
            required = True
            )
    severity = schema.Choice(
            title = u'Alert severity',
            description = u'Severity is based on criticality and fidelity',
            required = True,
            values=[u'low',u'medium',u'high',u'critical']
            )

class ISecurityAlert(IAlert):
    """An alert related to events with security implications"""