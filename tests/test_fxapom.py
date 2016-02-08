# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from mock import Mock

import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver

from fxapom.pages.sign_in import SignIn


@pytest.fixture
def webdriver(request):
    driver = Mock(spec=WebDriver)

    def element(*locator):
        element = Mock()
        element.is_displayed = Mock(return_value=True)
        return element

    driver.find_element = Mock(side_effect=element)
    return driver


def test_webdriver_with_fxa_popup(webdriver):
    webdriver.current_window_handle = 'bar'
    webdriver.window_handles = [1, 2]
    sign_in = SignIn(webdriver)
    assert sign_in._main_window_handle == 'bar'
    assert sign_in.popup is True
    webdriver.window_handles = [2]
    sign_in.sign_in('email', 'password')


def test_webdriver_fxa_popup_without_logo_present(webdriver):
    webdriver.window_handles = [1, 2]

    def missing_logo(*locator):
        if locator == SignIn._fox_logo_locator:
            raise NoSuchElementException
        element = Mock()
        element.is_displayed = Mock(return_value=True)
        return element

    webdriver.find_element = Mock(side_effect=missing_logo)
    with pytest.raises(Exception) as excinfo:
        SignIn(webdriver)
    assert 'Popup has not loaded' in str(excinfo.value)


def test_webdriver_fxa_popup_without_logo_displayed(webdriver):
    webdriver.window_handles = [1, 2]

    def hidden_logo(*locator):
        element = Mock()
        element.is_displayed = Mock(return_value=True)
        if locator == SignIn._fox_logo_locator:
            element.is_displayed.return_value = False
        return element

    webdriver.find_element = Mock(side_effect=hidden_logo)
    sign_in = SignIn(webdriver)
    webdriver.window_handles = [2]
    sign_in.sign_in('email', 'password')
