# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from marionette_driver import By, Wait
from marionette_driver.marionette import Marionette


@pytest.fixture
def click_login(base_url, marionette, timeout):
    fxa_login_button_locator = (By.CSS_SELECTOR, 'button.signin')
    marionette.navigate('%s/' % base_url)
    Wait(marionette, timeout).until(
        lambda m: m.find_element(*fxa_login_button_locator).is_displayed())
    marionette.find_element(*fxa_login_button_locator).click()


@pytest.fixture
def marionette(request):
    m = Marionette(bin=request.config.option.bin)
    m.start_session()
    m.set_prefs({'signon.rememberSignons': False})
    request.addfinalizer(m.delete_session)
    return m
