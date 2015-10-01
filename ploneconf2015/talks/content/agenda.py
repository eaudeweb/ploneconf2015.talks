""" Agenda
"""
from zope.interface import implementer
from plone.dexterity.content import Container
from ploneconf2015.talks.content.interfaces import IAgenda
from ploneconf2015.talks.content.interfaces import IAgendaDay

@implementer(IAgenda)
class Agenda(Container):
    """ Agenda content-type
    """

@implementer(IAgendaDay)
class AgendaDay(Container):
    """ Agenda Day content-type
    """
