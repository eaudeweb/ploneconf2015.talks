""" Author content-type
"""
from zope.interface import implementer
from plone.dexterity.content import Container
from ploneconf2015.talks.content.interfaces import IAuthor

@implementer(IAuthor)
class Author(Container):
    """ Author content-type
    """
