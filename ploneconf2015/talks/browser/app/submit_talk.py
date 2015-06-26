""" Submit Talk view
"""
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from plone.dexterity.utils import createContentInContainer
from Products.CMFCore.interfaces import IFolderish
from z3c.relationfield import RelationValue
from zope.intid.interfaces import IIntIds
from zope.component import getUtility
from plone.namedfile.file import NamedBlobImage
from datetime import datetime

class SubmitTalk(BrowserView):
    """ Submit Talk view
    """

    def submit(self):
        (speaker, index) = self.create_speaker()
        talk = self.create_talk(speaker, index)
        return (speaker, talk)

    def create_speaker(self):
        tool = getToolByName(self.context, u'portal_types')
        speaker_info = tool.getTypeInfo(u'speaker')

        if 'Speakers' not in self.context.keys():
            folder_info = tool.getTypeInfo(u'Folder')
            folder_info._constructInstance(self.context,
                    u'Speakers', title=u'Speakers')

        form = self.request.form
        for index in range(1, 10000):
            try:
                speaker = speaker_info._constructInstance(
                    self.context['Speakers'], u'speaker%.3d' % index,
                    title=form['name'], description=form['about'],
                    email=form['email'], country=form['country'],
                    company=form['company'], twitter=form['twitter'],
                    irc=form['irc'])
            except Exception:
                continue
            else:
                speaker.picture = NamedBlobImage(
                            filename=u"%s picture" % form['name'],
                            data=form['picture'].read())
                return (speaker, index)

    def create_talk(self, speaker, index):
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
        talk.relatedItems = [RelationValue(intids.getId(speaker))]
        return talk

    def __call__(self, **kwargs):
        if self.request.method.lower() != 'post':
            return self.index()

        (speaker, talk) = self.submit()
