# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from ploneconf2015.talks.testing import PLONECONF2015_TALKS_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that ploneconf2015.talks is properly installed."""

    layer = PLONECONF2015_TALKS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ploneconf2015.talks is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('ploneconf2015.talks'))

    def test_uninstall(self):
        """Test if ploneconf2015.talks is cleanly uninstalled."""
        self.installer.uninstallProducts(['ploneconf2015.talks'])
        self.assertFalse(self.installer.isProductInstalled('ploneconf2015.talks'))

    def test_browserlayer(self):
        """Test that IPloneconf2015TalksLayer is registered."""
        from ploneconf2015.talks.interfaces import IPloneconf2015TalksLayer
        from plone.browserlayer import utils
        self.assertIn(IPloneconf2015TalksLayer, utils.registered_layers())
