# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from tokyo2018.andre_package.testing import TOKYO2018_ANDRE_PACKAGE_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that tokyo2018.andre_package is properly installed."""

    layer = TOKYO2018_ANDRE_PACKAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if tokyo2018.andre_package is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'tokyo2018.andre_package'))

    def test_browserlayer(self):
        """Test that ITokyo2018AndrePackageLayer is registered."""
        from tokyo2018.andre_package.interfaces import (
            ITokyo2018AndrePackageLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ITokyo2018AndrePackageLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = TOKYO2018_ANDRE_PACKAGE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['tokyo2018.andre_package'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if tokyo2018.andre_package is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'tokyo2018.andre_package'))

    def test_browserlayer_removed(self):
        """Test that ITokyo2018AndrePackageLayer is removed."""
        from tokyo2018.andre_package.interfaces import \
            ITokyo2018AndrePackageLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            ITokyo2018AndrePackageLayer,
            utils.registered_layers())
