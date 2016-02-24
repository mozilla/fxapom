# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from selenium.webdriver.support.wait import WebDriverWait as Wait

from fxapom.fxapom import DEV_URL, FxATestAccount, PROD_URL, TIMEOUT


def pytest_addoption(parser):
    parser.addoption(
        '--bin',
        default='/usr/local/bin/firefox',
        help='path for Firefox binary')


@pytest.fixture(scope='session')
def session_capabilities(session_capabilities):
    session_capabilities.setdefault('tags', []).append('fxapom')
    return session_capabilities


@pytest.fixture(params=[DEV_URL, PROD_URL])
def account(request):
    return FxATestAccount(request.param)


@pytest.fixture
def dev_account():
    return FxATestAccount(DEV_URL)


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
