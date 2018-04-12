# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from selenium.webdriver.support.wait import WebDriverWait as Wait

from fxapom.fxapom import TIMEOUT


@pytest.fixture(scope='session')
def session_capabilities(pytestconfig, session_capabilities):
    if pytestconfig.getoption('driver') == 'SauceLabs':
        session_capabilities.setdefault('tags', []).append('fxapom')
    return session_capabilities


@pytest.fixture
def capabilities(request, capabilities):
    driver = request.config.getoption('driver')
    if capabilities.get('browserName', driver).lower() == 'firefox':
        capabilities['marionette'] = True
    return capabilities


@pytest.fixture
def timeout():
    return TIMEOUT


@pytest.fixture
def click_login(base_url, selenium, timeout):
    fxa_login_button_locator_css = 'button.signin'
    selenium.get('%s/' % base_url)
    Wait(selenium, timeout).until(
        lambda s: s.find_element_by_css_selector(fxa_login_button_locator_css).is_displayed())
    selenium.find_element_by_css_selector(fxa_login_button_locator_css).click()
