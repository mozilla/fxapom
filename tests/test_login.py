# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from fxapom.fxapom import FxATestAccount, WebDriverFxA


class TestLogin(object):

    _fxa_logged_in_indicator_locator = (By.ID, 'loggedin')

    def test_user_can_sign_in(self, mozwebqa):
        acct = FxATestAccount().create_account()
        fxa = WebDriverFxA(mozwebqa)
        fxa.sign_in(acct.email, acct.password)
        WebDriverWait(mozwebqa.selenium, mozwebqa.timeout).until(
            lambda s: s.find_element(*self._fxa_logged_in_indicator_locator).is_displayed())
