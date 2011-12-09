from zope import interface
from zope import schema

from plone.app.event.dx.behaviors import *
from plone.directives import form

from collective.opendataevent.i18n import _
from collective.opendataevent import vocabulary

class IOrganizer(form.schema):
    
    organizer_name = schema.TextLine(
        title = _(u'label_organizer_name', default=u'Organizer Name'),
        description = _(u'help_organizer_name', default=u'Name of a person to organizer about this event.'),
        required = False
        )

    organizer_email = schema.TextLine(
        title = _(u'label_organizer_email', default=u'Organizer E-mail'),
        description = _(u'help_organizer_email', default=u'Email address to organizer about this event.'),
        required = False
        )

    organizer_phone = schema.TextLine(
        title = _(u'label_organizer_phone', default=u'Organizer Phone'),
        description = _(u'help_organizer_phone', default=u'Phone number to organizer about this event.'),
        required = False
        )

    organizer_url = schema.TextLine(
        title = _(u'label_organizer_url', default=u'Organizer URL'),
        description = _(u'help_event_url', default=u'Web address of the organizer.'),
        required = False
        )

    organizer_role = schema.Choice(title=_(u'label_organizer'),
                                   vocabulary="collective.opendataevent.vocabulary.organizerrole")

class IEventBehavior(IEventBasic, IEventLocation, IEventAttendees, IEventorganizer):
    """ Full Event Behavior.

    """
    form.fieldset(
            'event',
            label=_(u'label_fieldset_event', default=u'Event'),
            fields=(
                'start',
                'end',
                'timezone',
                'recurrence',
                'whole_day',
                'location',
                'attendees',
                'event_url',
                'contact_name',
                'contact_email',
                'contact_phone',
                ),
        )
