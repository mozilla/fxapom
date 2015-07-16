# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import re

import pytest

from fxapom.fxapom import AccountNotFoundException, DEV_URL, FxATestAccount


@pytest.mark.skip_selenium
class TestFxATestAccount(object):

    def test_default_environment_should_be_dev(self):
        account = FxATestAccount()
        assert DEV_URL == account.url

    def test_create_new_account(self, account):
        assert account.is_verified
        # Test logging in - will throw an exception if log in fails
        account.login()

    def test_new_account_pw_does_not_contain_numbers(self, dev_account):
        assert re.search(r'\d', dev_account.password) is None

    def test_delete_account(self, account):
        account.delete_account()
        with pytest.raises(AccountNotFoundException):
            account.login()
