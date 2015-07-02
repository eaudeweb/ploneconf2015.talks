""" Content rules adapters
"""
from plone.stringinterp.adapters import BaseSubstitution

class SubmitTalkSubstitution(BaseSubstitution):
    """ Submit talk string substitution
    """
    def __init__(self, context, **kwargs):
        super(SubmitTalkSubstitution, self).__init__(context, **kwargs)

    @property
    def talkTitle(self):
        return self.context.title

    @property
    def speakerEmail(self):
        return self.context.relatedItems[0].to_object.email

    def safe_call(self):
        """ Safe call
        """
        return getattr(self, self.attribute, u'')
#
# String substitution adapters
#
class TalkTitle(SubmitTalkSubstitution):
    """ Submitted talk title
    """
    category = u'Submitted Talks'
    description = u'Submitted talk title'
    attribute = u'talkTitle'

class SpeakerEmail(SubmitTalkSubstitution):
    """ Submitted talk speaker email
    """
    category = u'Submitted Talks'
    description = u'Submitted talk speaker email'
    attribute = u'speakerEmail'
