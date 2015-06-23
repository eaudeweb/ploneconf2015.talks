# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s ploneconf2015.talks -t test_talk.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src ploneconf2015.talks.testing.PLONECONF2015_TALKS_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_talk.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Talk
  Given a logged-in site administrator
    and an add talk form
   When I type 'My Talk' into the title field
    and I submit the form
   Then a talk with the title 'My Talk' has been created

Scenario: As a site administrator I can view a Talk
  Given a logged-in site administrator
    and a talk 'My Talk'
   When I go to the talk view
   Then I can see the talk title 'My Talk'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add talk form
  Go To  ${PLONE_URL}/++add++Talk

a talk 'My Talk'
  Create content  type=Talk  id=my-talk  title=My Talk


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the talk view
  Go To  ${PLONE_URL}/my-talk
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a talk with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the talk title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
