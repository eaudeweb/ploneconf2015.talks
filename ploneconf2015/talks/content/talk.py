""" Talk content-type
"""
from zope.interface import implementer
from plone.dexterity.content import Container
from ploneconf2015.talks.content.interfaces import ITalk

@implementer(ITalk)
class Talk(Container):
    """ Talk content-type
    """
