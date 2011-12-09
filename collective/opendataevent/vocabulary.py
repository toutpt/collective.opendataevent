from zope import interface
from zope.schema.interfaces import IVocabularyFactory

from zope.schema.vocabulary import getVocabularyRegistry
from plone.app.vocabularies import language

ORGANIZER_ROLE_ID='collective.opendataevent.vdexvocabulary.organizerrole'

class OrganizerRoleVocabulary(object):
    interface.implements(IVocabularyFactory)

    def __call__(self, context):
        vr = getVocabularyRegistry()
        roles = vr.get(self.context, ORGANIZER_ROLE_ID)
        return roles


OrganizerRoleVocabularyFactory = OrganizerRoleVocabulary()
