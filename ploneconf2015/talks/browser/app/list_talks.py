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

    def __call__(self, **kwargs):
        return self.index()