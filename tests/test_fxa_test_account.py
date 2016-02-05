# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait

from fxapom.fxapom import DEV_URL, FxATestAccount, WebDriverFxA


class TestFxATestAccount(object):

    _fxa_unknown_account_error_locator = (By.CSS_SELECTOR, '#main-content div.error')

    def test_default_environment_should_be_dev(self):
        account = FxATestAccount()
        assert DEV_URL == account.url

    def test_create_new_account(self, account):
        assert account.is_verified
        # Test logging in - will throw an exception if log in fails
        account.login()

    def test_new_account_pw_does_not_contain_numbers(self, account):
        assert re.search(r'\d', account.password) is None

    def test_del(self, selenium, click_login, timeout):
        """ Check that the __del__ method does destroy the FxA """
        account = FxATestAccount()
        email = account.email
        password = account.password

        # destroy account
        del account

        # try to log in
        fxa = WebDriverFxA(selenium)
        fxa.sign_in(email, password)
        el = Wait(selenium, timeout).until(
            EC.visibility_of_element_located(self._fxa_unknown_account_error_locator))
        assert 'Unknown account' in el.text
