# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import re

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from fxapom.fxapom import DEV_URL, FxATestAccount, WebDriverFxA


class TestFxATestAccount(object):

    _fxa_unknown_account_error_locator = (By.CSS_SELECTOR, '#main-content div.error')

    @pytest.mark.skip_selenium
    def test_default_environment_should_be_dev(self):
        account = FxATestAccount()
        assert DEV_URL == account.url

    @pytest.mark.skip_selenium
    def test_create_new_account(self, account):
        assert account.is_verified
        # Test logging in - will throw an exception if log in fails
        account.login()

    @pytest.mark.skip_selenium
    def test_new_account_pw_does_not_contain_numbers(self, account):
        assert re.search(r'\d', account.password) is None

    def test_del(self, mozwebqa):
        """ Check that the __del__ method does destroy the FxA """
        account = FxATestAccount()
        email = account.email
        password = account.password

        # destroy account
        del account

        # try to log in
        fxa = WebDriverFxA(mozwebqa)
        fxa.sign_in(email, password)
        WebDriverWait(mozwebqa.selenium, mozwebqa.timeout).until(
            lambda s: s.find_element(*self._fxa_unknown_account_error_locator).is_displayed())
        assert 'Unknown account' in mozwebqa.selenium.find_element(*self._fxa_unknown_account_error_locator).text
