# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.common.exceptions import NoSuchElementException

from ..fxapom import TIMEOUT


class Page(object):

    def __init__(self, base_url, selenium, timeout=TIMEOUT):
        self.base_url = base_url
        self.selenium = selenium
        self.timeout = timeout
        self._selenium_root = hasattr(self, '_root_element') and self._root_element or self.selenium

    def is_element_visible(self, *locator):
        try:
            return self._selenium_root.find_element(*locator).is_displayed()
        except (NoSuchElementException,):
            return False
