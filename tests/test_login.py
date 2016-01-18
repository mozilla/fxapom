# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait

from fxapom.fxapom import WebDriverFxA


class TestLogin(object):

    _fxa_logged_in_indicator_locator = (By.ID, 'loggedin')

    def test_user_can_sign_in(self, selenium, dev_account, click_login, timeout):
        fxa = WebDriverFxA(selenium, timeout)
        fxa.sign_in(dev_account.email, dev_account.password)
        # We sometimes need to wait longer than the standard 10 seconds
        Wait(selenium, timeout).until(
            EC.visibility_of_element_located(self._fxa_logged_in_indicator_locator))
