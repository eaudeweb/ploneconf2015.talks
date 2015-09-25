""" Speaker view
"""
from Products.Five.browser import BrowserView

class Speaker(BrowserView):
    """ Speaker view
    """

    @property
    def name(self):
        return self.context.title

    @property
    def summary(self):
        return self.context.description

    @property
    def email(self):
        return self.context.email

    @property
    def country(self):
        return self.context.country

    @property
    def twitter(self):
        value = self.context.twitter
        if not value:
            return u''

        if value.startswith('http'):
            value = value.split('/')[-1]

        value = value.strip('@')
        return value

    @property
    def github(self):
        value = self.context.git
        if not value:
            return u''

        if value.startswith('http'):
            value = value.split('/')[-1]

        value = value.strip('@')
        return value

    @property
    def git(self):
        return self.context.git

    @property
    def linkedin(self):
        return self.context.linkedin

    @property
    def image(self):
        if self.context.image:
            return self.context.absolute_url() + '/@@images/image/'
        return ''

    def __call__(self, **kwargs):
        return self.index()
