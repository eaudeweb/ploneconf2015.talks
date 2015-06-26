""" Speaker content-type
"""
from zope.interface import implementer
from plone.dexterity.content import Container
from ploneconf2015.talks.content.interfaces import ISpeaker

@implementer(ISpeaker)
class Speaker(Container):
    """ Speaker content-type
    """
