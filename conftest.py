# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.support.ui import WebDriverWait


def pytest_funcarg__mozwebqa(request):
    fxa_login_button_locator_css = 'button.signin'
    mozwebqa = request.getfuncargvalue('mozwebqa')
    mozwebqa.selenium.get('%s/' % mozwebqa.base_url)
    WebDriverWait(mozwebqa.selenium, mozwebqa.timeout).until(
        lambda s: s.find_element_by_css_selector(fxa_login_button_locator_css).is_displayed())
    mozwebqa.selenium.find_element_by_css_selector(fxa_login_button_locator_css).click()
    return mozwebqa
