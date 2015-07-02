""" Submit Talk event
"""
from zope.interface import implements
from ploneconf2015.talks.events import interfaces

class SubmitTalkEvent(object):
    """ Submit Talk event
    """
    implements(interfaces.ISubmitTalkEvent)

    def __init__(self, context, **kwargs):
        self.object = context
