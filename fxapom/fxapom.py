# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import string
import random
from datetime import datetime

from fxa.core import Client
from fxa.tests.utils import TestEmailAccount


# Constants for available FxA environments
DEV_URL = 'https://stable.dev.lcip.org/auth/'
PROD_URL = 'https://api.accounts.firefox.com/'


class WebDriverFxA(object):

    def __init__(self, testsetup):
        self.testsetup = testsetup

    def sign_in(self, email=None, password=None):
        """Signs in a user, either with the specified email address and password, or a returning user."""
        from pages.sign_in import SignIn
        sign_in = SignIn(self.testsetup)
        sign_in.sign_in(email, password)


class FxATestAccount:
    """A base test class that can be extended by other tests to include utility methods."""

    password = ''.join([random.choice(string.letters) for i in range(8)])

    def __init__(self, url=DEV_URL):
        """ Creates an FxATestAccount object.

        :param url: The url for the api host. Defaults to DEV_URL.
        """
        self.url = url

    def create_account(self):
        random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(12))
        email_pattern = random_string + '@{hostname}'
        self.account = TestEmailAccount(email=email_pattern)
        client = Client(self.url)
        # Create and verify the Firefox account
        self.session = client.create_account(self.account.email, self.password)
        print 'fxapom created an account for email: %s at %s on %s' % (
            self.account.email, self.url, datetime.now())
        m = self.account.wait_for_email(lambda m: "x-verify-code" in m["headers"])
        if not m:
            raise RuntimeError("Verification email was not received")
        self.session.verify_email_code(m["headers"]["x-verify-code"])
        return self

    @property
    def email(self):
        return self.account.email

    @property
    def is_verified(self):
        return self.session.get_email_status()['verified']
