""" List Talks view
"""
from Products.Five.browser import BrowserView

class ListTalks(BrowserView):
    """ List Talks view
    """
    @property
    def speakers_and_talk(self):
        try:
            brains = self.context['Talks'].getFolderContents()
        except Exception:
            return []
        speakers_and_talk = []
        for brain in brains:
            talk = brain.getObject()
            speakers = [talk.relatedItems[i].to_object for i in range(len(talk.relatedItems))]
            speakers_and_talk.append((speakers, talk))
        return speakers_and_talk

    def cleanup(self, value):
        """ Cleanup value
        """
        if not value:
            return u''

        if value.startswith('http'):
            value = value.split('/')[-1]

        value = value.strip('@')
        return value

    def twitter(self, value):
        """ Parse twitter account
        """
        return self.cleanup(value)

    def github(self, value):
        """ Parse twitter account
        """
        return self.cleanup(value)

    def __call__(self, **kwargs):
        return self.index()
