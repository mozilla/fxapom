# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.common.exceptions import NoSuchElementException

from fxapom.fxapom import TIMEOUT


class Page(object):

    def __init__(self, selenium, timeout=TIMEOUT):
        self.selenium = selenium
        self.timeout = timeout

    def is_element_visible(self, *locator):
        try:
            return self.selenium.find_element(*locator).is_displayed()
        except (NoSuchElementException,):
            return False
