# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from fxapom.fxapom import WebDriverFxA


class TestLogin(object):

    _fxa_logged_in_indicator_locator = (By.ID, 'loggedin')

    def test_user_can_sign_in(self, base_url, selenium, dev_account, click_login):
        fxa = WebDriverFxA(base_url, selenium)
        fxa.sign_in(dev_account.email, dev_account.password)
        WebDriverWait(selenium, 20).until(
            lambda s: s.find_element(*self._fxa_logged_in_indicator_locator).is_displayed())
