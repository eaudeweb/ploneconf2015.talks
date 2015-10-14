""" Speaker view
"""
from Products.Five.browser import BrowserView

class Talk(BrowserView):
    """ Speaker view
    """

    def speakers(self):
        """ Speakers
        """
        for speaker in self.context.relatedItems:
            yield speaker.to_object

    def twitter(self, speaker):
        value = speaker.twitter
        if not value:
            return u''

        if value.startswith('http'):
            value = value.split('/')[-1]

        value = value.strip('@')
        return value

    def github(self, speaker):
        value = speaker.git
        if not value:
            return u''

        if value.startswith('http'):
            value = value.split('/')[-1]

        value = value.strip('@')
        return value

    def video(self):
        """ Video
        """
        return self.context.video

    def slides(self):
        """ Slides
        """
        return self.context.slides
