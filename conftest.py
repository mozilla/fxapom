# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from selenium.webdriver.support.ui import WebDriverWait

from fxapom.fxapom import DEV_URL, FxATestAccount, PROD_URL


def pytest_funcarg__mozwebqa(request):
    fxa_login_button_locator_css = 'button.signin'
    mozwebqa = request.getfuncargvalue('mozwebqa')
    mozwebqa.selenium.get('%s/' % mozwebqa.base_url)
    WebDriverWait(mozwebqa.selenium, mozwebqa.timeout).until(
        lambda s: s.find_element_by_css_selector(fxa_login_button_locator_css).is_displayed())
    mozwebqa.selenium.find_element_by_css_selector(fxa_login_button_locator_css).click()
    return mozwebqa


@pytest.fixture(params=[DEV_URL, PROD_URL])
def account(request):
    account = FxATestAccount(request.param).create_account()

    def fin():
        account.delete_account()
    request.addfinalizer(fin)

    return account


@pytest.fixture
def dev_account(request):
    account = FxATestAccount(DEV_URL).create_account()

    def fin():
        account.delete_account()
    request.addfinalizer(fin)

    return account
