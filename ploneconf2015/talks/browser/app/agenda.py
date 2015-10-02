""" Agenda controllers
"""
import logging
from zope.component.hooks import getSite
from Products.Five.browser import BrowserView
logger = logging.getLogger('ploneconf2015.talks')

class Agenda(BrowserView):
    """ Agenda
    """
    def trainings(self):
        """ Trainings
        """
        for item in self.context.objectValues():
            if 'training' in item.getId():
                yield item

    def conferences(self):
        """ Trainings
        """
        for item in self.context.objectValues():
            if 'conference' in item.getId():
                yield item

    def sprints(self):
        """ Trainings
        """
        for item in self.context.objectValues():
            if 'sprint' in item.getId():
                yield item

class AgendaDay(BrowserView):
    """ Agenda Day
    """
    def listing(self):
        """ List items
        """
        hour = 0
        minute = 0
        for item in self.context.objectValues():
            if item.start.hour != hour or item.start.minute != minute:
                hour = item.start.hour
                minute = item.start.minute
                yield u"%d:%.2d" % (hour, minute)
            yield item

    def title(self, item):
        """ Get item title
        """
        if item.relatedItems:
            return item.relatedItems[0].to_object.title
        return item.title

    def link(self, item):
        """ Get item link
        """
        url = ''
        if item.relatedItems:
            site = getSite()
            rel = item.relatedItems[0].to_object
            try:
                url = site['talks'].absolute_url() + '#%s' % rel.getId()
            except Exception, err:
                logger.exception(err)
        return url

    def audience(self, item):
        """ Get item link
        """
        if item.relatedItems:
            return item.relatedItems[0].to_object.target_audience
        return []

class AgendaSlot(BrowserView):
    """ Agenda Slot
    """
