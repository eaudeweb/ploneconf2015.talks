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
        return self.context.twitter

    @property
    def git(self):
        return self.context.git

    @property
    def linkedin(self):
        return self.context.linkedin

    @property
    def image(self):
        return self.context.absolute_url() + '/@@images/image/'

    def __call__(self, **kwargs):
        return self.index()