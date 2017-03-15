# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected

from fxapom.fxapom import TIMEOUT
from fxapom.pages.base import Base


class SignIn(Base):

    _fox_logo_locator = (By.ID, 'fox-logo')
    _email_input_locator = (By.CSS_SELECTOR, '.input-row .email')
    _next_button_locator = (By.ID, 'email-button')
    _password_input_locator = (By.ID, 'password')
    _sign_in_locator = (By.ID, 'submit-btn')

    def __init__(self, selenium, timeout=TIMEOUT):
        super(SignIn, self).__init__(selenium, timeout)
        self._sign_in_window_handle = None
        self.popup = False
        self.check_for_popup(self.selenium.window_handles)

    @property
    def login_password(self):
        """Get the value of the login password field."""
        return self.selenium.find_element(*self._password_input_locator).get_attribute('value')

    @login_password.setter
    def login_password(self, value):
        """Set the value of the login password field."""
        password = self.selenium.find_element(*self._password_input_locator)
        password.clear()
        password.send_keys(value)

    def click_next(self):
        self.selenium.find_element(*self._next_button_locator).click()

    @property
    def email(self):
        """Get the value of the email field."""
        return self.selenium.find_element(*self._email_input_locator).get_attribute('value')

    @email.setter
    def email(self, value):
        """Set the value of the email field."""
        email = self.wait.until(expected.visibility_of_element_located(
            self._email_input_locator))
        email.clear()
        email.send_keys(value)

    def check_for_popup(self, handles):
        if len(handles) > 1:
            self.popup = True
            for handle in handles:
                self.selenium.switch_to.window(handle)
                if self.is_element_present(*self._fox_logo_locator):
                    self._sign_in_window_handle = handle
                    break
            else:
                raise Exception('Popup has not loaded')
        self.wait.until(expected.visibility_of_element_located(
            self._email_input_locator))

    def click_sign_in(self):
        self.selenium.find_element(*self._sign_in_locator).click()
        if self.popup:
            self.wait.until(
                lambda s: self._sign_in_window_handle not in self.selenium.window_handles)
            self.switch_to_main_window()

    def sign_in(self, email, password):
        """Signs in using the specified email address and password."""
        self.email = email
        self.login_password = password
        if self.is_element_present(*self._next_button_locator):
            self.wait.until(expected.visibility_of_element_located(
                self._next_button_locator))
            self.click_next()
        self.click_sign_in()
