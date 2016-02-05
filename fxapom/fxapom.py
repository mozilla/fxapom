
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import string
import random
from datetime import datetime

from fxa.core import Client
from fxa.errors import ClientError
from fxa.tests.utils import TestEmailAccount

from selenium.webdriver.remote.webdriver import WebDriver

# Constants for available FxA environments
DEV_URL = 'https://stable.dev.lcip.org/auth/'
PROD_URL = 'https://api.accounts.firefox.com/'

TIMEOUT = 20


class AccountNotFoundException(Exception):
    pass


class WebDriverFxA(object):

    def __init__(self, driver, timeout=TIMEOUT):
        self.driver = driver
        self.timeout = timeout

    def sign_in(self, email=None, password=None):
        """Signs in a user, either with the specified email address and password, or a returning user."""
        if isinstance(self.driver, WebDriver):
            from pages.sign_in import SignIn
        else:
            from pages.marionette.sign_in import MarionetteSignIn as SignIn
        sign_in = SignIn(self.driver, self.timeout)
        sign_in.sign_in(email, password)


class FxATestAccount:
    """A base test class that can be extended by other tests to include utility methods."""

    password = ''.join([random.choice(string.letters) for i in range(8)])

    def __init__(self, url=DEV_URL):
        """ Creates an FxATestAccount object, which includes a verified account.

        :param url: The url for the api host. Defaults to DEV_URL.
        """
        self.url = url
        random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(12))
        email_pattern = random_string + '@{hostname}'
        self.account = TestEmailAccount(email=email_pattern)
        self.client = Client(self.url)
        # Create and verify the Firefox account
        self.session = self.client.create_account(self.account.email, self.password)
        print 'fxapom created an account for email: %s at %s on %s' % (
            self.account.email, self.url, datetime.now())
        m = self.account.wait_for_email(lambda m: "x-verify-code" in m["headers"])
        if not m:
            raise RuntimeError("Verification email was not received")
        self.session.verify_email_code(m["headers"]["x-verify-code"])

    def __del__(self):
        """ Deletes the Firefox Account that was created during __init__. """
        try:
            self.account.clear()
            self.client.destroy_account(self.email, self.password)
            print 'fxapom deleted the account for email: %s at %s on %s' % (
                self.account.email, self.url, datetime.now())
        except ClientError as err:
            # 'Unknown Account' error is ok - account already deleted
            # https://github.com/mozilla/fxa-auth-server/blob/master/docs/api.md#response-format
            if err.errno == 102:
                return
            raise

    def login(self):
        try:
            session = self.client.login(self.email, self.password)
            return session
        except ClientError as err:
            # 'Unknown Account' error is the only one we care about and will
            # cause us to throw a custom exception
            # https://github.com/mozilla/fxa-auth-server/blob/master/docs/api.md#response-format
            if err.errno == 102:
                raise AccountNotFoundException('FxA Account Not Found')
            raise

    @property
    def email(self):
        return self.account.email

    @property
    def is_verified(self):
        return self.session.get_email_status()['verified']
