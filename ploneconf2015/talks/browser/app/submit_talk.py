''' Submit Talk view
'''
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from plone.dexterity.utils import createContentInContainer
from Products.CMFCore.interfaces import IFolderish
from z3c.relationfield import RelationValue
from zope.intid.interfaces import IIntIds
from zope.component import getUtility
from datetime import datetime

class SubmitTalk(BrowserView):
    """ Submit Talk view
    """

    def submit(self):
        (author, index) = self.create_author()
        talk = self.create_talk(author, index)
        return (author, talk)

    def create_author(self):
        tool = getToolByName(self.context, u'portal_types')
        author_info = tool.getTypeInfo(u'author')

        if 'Authors' not in self.context.keys():
            folder_info = tool.getTypeInfo(u'Folder')
            folder_info._constructInstance(self.context,
                    u'Authors', title=u'Authors')

        form = self.request.form
        for index in range(1, 10000):
            try:
                author = author_info._constructInstance(
                    self.context['Authors'], u'author%.3d' % index,
                    title=form['name'], description=form['about'],
                    email=form['email'], country=form['country'],
                    company=form['company'], twitter=form['twitter'],
                    irc=form['irc'])
            except Exception:
                continue
            else:
                return (author, index)

    def create_talk(self, author, index):
        tool = getToolByName(self.context, u'portal_types')
        talk_info = tool.getTypeInfo(u'talk')

        if 'Talks' not in self.context.keys():
            folder_info = tool.getTypeInfo(u'Folder')
            folder_info._constructInstance(self.context,
                    u'Talks', title=u'Talks')

        form = self.request.form
        talk = talk_info._constructInstance(
            self.context['Talks'], u'talk%.3d' % index,
            title=form['talk_title'], description=form['talk_summary'],
            target_audience=form['talk_audience'])

        intids = getUtility(IIntIds)
        talk.relatedItems = [RelationValue(intids.getId(author))]
        return talk

    def __call__(self, **kwargs):
        if self.request.method.lower() != 'post':
            return self.index()

        (author, talk) = self.submit()
