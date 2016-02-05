# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from fxapom.fxapom import TIMEOUT
from fxapom.pages.marionette.page import Page


class Base(Page):

    def __init__(self, driver, timeout=TIMEOUT):
        super(Page, self).__init__(driver, timeout)
        self._main_window_handle = self.driver.current_window_handle

    def switch_to_main_window(self):
        self.driver.switch_to_window(self._main_window_handle)

    def close_window(self):
        self.driver.close()
