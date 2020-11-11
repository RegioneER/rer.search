# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import rer.search


class RerSearchLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=rer.search)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'rer.search:default')


RER_SEARCH_FIXTURE = RerSearchLayer()


RER_SEARCH_INTEGRATION_TESTING = IntegrationTesting(
    bases=(RER_SEARCH_FIXTURE,),
    name='RerSearchLayer:IntegrationTesting',
)


RER_SEARCH_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(RER_SEARCH_FIXTURE,),
    name='RerSearchLayer:FunctionalTesting',
)


RER_SEARCH_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        RER_SEARCH_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='RerSearchLayer:AcceptanceTesting',
)
