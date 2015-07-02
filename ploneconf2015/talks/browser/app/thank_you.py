""" Submission Thanks view
"""
from Products.Five.browser import BrowserView

class ThankYou(BrowserView):
    """ Submission Thanks view
    """

    def __call__(self, **kwargs):
        if self.request.get_header('referer') is None or 'submit-talk' not in self.request.get_header('referer'):
            self.request.response.redirect(self.context.absolute_url() + '/submit-talk/')
        return self.index()
