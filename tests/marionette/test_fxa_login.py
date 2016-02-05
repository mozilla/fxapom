# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from marionette_driver import By, expected, Wait

from fxapom.fxapom import WebDriverFxA


class TestLogin(object):

    _fxa_logged_in_indicator_locator = (By.ID, 'loggedin')

    def test_user_can_sign_in(self, base_url, marionette, dev_account, click_login, timeout):
        fxa = WebDriverFxA(marionette, timeout)
        fxa.sign_in(dev_account.email, dev_account.password)
        # We sometimes need to wait longer than the standard 10 seconds
        logged_in = Wait(marionette, timeout).until(
            expected.element_present(*self._fxa_logged_in_indicator_locator))
        Wait(marionette, timeout).until(expected.element_displayed(logged_in))
