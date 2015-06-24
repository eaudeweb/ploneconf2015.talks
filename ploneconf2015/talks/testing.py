# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import ploneconf2015.talks


class Ploneconf2015TalksLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=ploneconf2015.talks)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ploneconf2015.talks:default')


PLONECONF2015_TALKS_FIXTURE = Ploneconf2015TalksLayer()


PLONECONF2015_TALKS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONECONF2015_TALKS_FIXTURE,),
    name='Ploneconf2015TalksLayer:IntegrationTesting'
)


PLONECONF2015_TALKS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONECONF2015_TALKS_FIXTURE,),
    name='Ploneconf2015TalksLayer:FunctionalTesting'
)


PLONECONF2015_TALKS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONECONF2015_TALKS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='Ploneconf2015TalksLayer:AcceptanceTesting'
)
