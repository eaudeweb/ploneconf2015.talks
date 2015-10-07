""" Agenda controllers
"""
import logging
from zope.component.hooks import getSite
from Products.Five.browser import BrowserView
logger = logging.getLogger('ploneconf2015.talks')

class Agenda(BrowserView):
    """ Agenda
    """
    def trainings(self, context=None):
        """ Trainings
        """
        if not context:
            context = self.context

        for item in context.objectValues():
            if 'training' in item.getId():
                yield item

    def conferences(self, context=None):
        """ Conf days
        """
        if not context:
            context = self.context

        for item in context.objectValues():
            if 'conference' in item.getId():
                yield item

    def sprints(self, context=None):
        """ Sprints
        """
        if not context:
            context = self.context

        for item in context.objectValues():
            if 'sprint' in item.getId():
                yield item

class AgendaDay(Agenda):
    """ Agenda Day
    """
    def trainings(self, context=None):
        """ Trainings
        """
        if not context:
            context = self.context.getParentNode()
        return super(AgendaDay, self).trainings(context=context)

    def conferences(self, context=None):
        """ Trainings
        """
        if not context:
            context = self.context.getParentNode()
        return super(AgendaDay, self).conferences(context=context)

    def sprints(self, context=None):
        """ Sprints
        """
        if not context:
            context = self.context.getParentNode()
        return super(AgendaDay, self).sprints(context=context)

    def current(self, item):
        """ Is current item?
        """
        if self.context.getId() == item.getId():
            return True
        return False

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

    def speakers(self, item):
        """ Get item authors
        """
        if not item.relatedItems:
            return

        talk = item.relatedItems[0].to_object
        if not getattr(talk, 'relatedItems', None):
            return

        for speaker in talk.relatedItems:
            yield speaker.to_object

    def start(self, item, delimiter=':'):
        """ Start time
        """
        hour = item.start.hour
        minute = item.start.minute
        return u"%d%s%.2d" % (hour, delimiter, minute)

    def end(self, item, delimiter=':'):
        """ End time
        """
        hour = item.end.hour
        minute = item.end.minute
        return u"%d%s%.2d" % (hour, delimiter, minute)

    def slot(self, item):
        """ Slot type
        """
        stype = 'single'
        start = item.start
        count = 0
        for talk in self.listing():
            if not hasattr(talk, 'start'):
                continue

            if talk.start == start:
                count += 1
            elif talk.start > start:
                break

        if count > 1:
            return 'multiple'
        return 'single'

class AgendaSlot(BrowserView):
    """ Agenda Slot
    """
