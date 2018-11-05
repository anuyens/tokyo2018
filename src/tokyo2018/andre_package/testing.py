# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import tokyo2018.andre_package


class Tokyo2018AndrePackageLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=tokyo2018.andre_package)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'tokyo2018.andre_package:default')


TOKYO2018_ANDRE_PACKAGE_FIXTURE = Tokyo2018AndrePackageLayer()


TOKYO2018_ANDRE_PACKAGE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(TOKYO2018_ANDRE_PACKAGE_FIXTURE,),
    name='Tokyo2018AndrePackageLayer:IntegrationTesting',
)


TOKYO2018_ANDRE_PACKAGE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(TOKYO2018_ANDRE_PACKAGE_FIXTURE,),
    name='Tokyo2018AndrePackageLayer:FunctionalTesting',
)


TOKYO2018_ANDRE_PACKAGE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        TOKYO2018_ANDRE_PACKAGE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='Tokyo2018AndrePackageLayer:AcceptanceTesting',
)
