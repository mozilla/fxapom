# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import re

import pytest

from fxapom.fxapom import DEV_URL, FxATestAccount, PROD_URL


@pytest.mark.skip_selenium
class TestCreateAccount(object):

    def test_default_environment_should_be_dev(self):
        acct = FxATestAccount()
        assert DEV_URL == acct.url

    def test_create_new_account_on_dev(self):
        acct = FxATestAccount(DEV_URL).create_account()
        assert acct.is_verified
        assert DEV_URL == acct.url

    def test_create_new_account_on_prod(self):
        acct = FxATestAccount(PROD_URL).create_account()
        assert acct.is_verified
        assert PROD_URL == acct.url

    def test_new_account_pw_does_not_contain_numbers(self):
        acct = FxATestAccount().create_account()
        test_regex = re.compile('\d')
        assert test_regex.search(acct.password) is None
