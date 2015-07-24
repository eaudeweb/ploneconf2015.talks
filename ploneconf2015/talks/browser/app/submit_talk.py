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
from zope.container.interfaces import INameChooser
from ploneconf2015.talks.events.submit_talk import SubmitTalkEvent
from zope.event import notify
import requests
import json


class SubmitTalk(BrowserView):
    """ Submit Talk view
    """

    def submit(self):
        self.create_talk(speakers=self.create_speakers())

    def create_speakers(self):
        tool = getToolByName(self.context, u'portal_types')
        speaker_info = tool.getTypeInfo(u'speaker')

        if 'Speakers' not in self.context.keys():
            folder_info = tool.getTypeInfo(u'Folder')
            folder_info._constructInstance(self.context,
                    u'Speakers', title=u'Speakers')

        form = self.request.form
        speakers = []
        for index in range(0, 100):
            if 'speaker_name' + str(index) not in form:
                break
            speakers.append(speaker_info._constructInstance(
                self.context['Speakers'],
                id=INameChooser(self.context['Speakers']).chooseName(form['speaker_name' + str(index)], self.context),
                title=form['speaker_name' + str(index)], description=form['speaker_about' + str(index)],
                email=form['speaker_email' + str(index)], country=form['speaker_country' + str(index)],
                company=form['speaker_company' + str(index)], twitter=form['speaker_twitter' + str(index)],
                git=form['speaker_git' + str(index)], linkedin=form['speaker_linkedin' + str(index)]))

            if 'speaker_buddy' + str(index) in form:
                speakers[index].buddy = True
            if 'speaker_first_time' + str(index) in form:
                speakers[index].first_time = True

            if form['speaker_image' + str(index)]:
                speakers[index].image = NamedBlobImage(
                            filename=form['speaker_name' + str(index)].decode('utf-8') + u' image',
                            data=requests.get(form['speaker_image' + str(index)]).content)

        return speakers

    def create_talk(self, speakers):
        tool = getToolByName(self.context, u'portal_types')
        talk_info = tool.getTypeInfo(u'talk')

        if 'Talks' not in self.context.keys():
            folder_info = tool.getTypeInfo(u'Folder')
            folder_info._constructInstance(self.context,
                    u'Talks', title=u'Talks')

        form = self.request.form
        talk = talk_info._constructInstance(
            self.context['Talks'],
            id=INameChooser(self.context['Talks']).chooseName(form['talk_title'], self.context),
            title=form['talk_title'], description=form['talk_summary'])

        talk.target_audience = json.loads(form['talk_audience']).values()

        intids = getUtility(IIntIds)
        talk.relatedItems = [RelationValue(intids.getId(speaker)) for speaker in speakers]

        notify(SubmitTalkEvent(context=talk))

    def __call__(self, **kwargs):
        if self.request.method.lower() != 'post':
            return self.index()
        self.submit()
        self.request.response.redirect(self.context.absolute_url() + '/thank-you')
