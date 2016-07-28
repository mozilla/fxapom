Firefox Accounts Page Object Model
==================================

`Selenium WebDriver <http://docs.seleniumhq.org/docs/03_webdriver.jsp>`_ compatible page object model and utilities for `Firefox Accounts <https://accounts.firefox.com>`_

.. image:: https://img.shields.io/pypi/l/fxapom.svg
   :target: https://github.com/mozilla/fxapom/blob/master/LICENSE
   :alt: License
.. image:: https://img.shields.io/pypi/v/fxapom.svg
   :target: https://pypi.python.org/pypi/fxapom/
   :alt: PyPI
.. image:: https://img.shields.io/travis/mozilla/fxapom.svg
   :target: https://travis-ci.org/mozilla/fxapom/
   :alt: Travis
.. image:: https://img.shields.io/github/issues-raw/mozilla/fxapom.svg
   :target: https://github.com/mozilla/fxapom/issues
   :alt: Issues
.. image:: https://img.shields.io/requires/github/mozilla/fxapom.svg
   :target: https://requires.io/github/mozilla/fxapom/requirements/?branch=master
   :alt: Requirements

Overview
--------

This package contains a utility to create a test Firefox Account on either the dev or prod instance of Firefox Accounts,
as well as a set of page objects that can be used to interact with Firefox Accounts' sign in screens.

Installation
------------

``python setup.py develop``

**If running on a Mac, you may need the following before running the above command:**

``pip install cryptography``

Usage
-----

To create a test Firefox Account, simply create an instance of the ``FxATestAccount`` object.
You can pass the url for the Firefox Accounts API server into the constructor
or, if you know you want to create a development Account, you can omit that argument.

There are two constants available to you to specify the url for either the development environment
or the production environment, which are:

* ``fxapom.DEV_URL`` - the url for the development environment
* ``fxapom.PROD_URL`` - the url for the production environment

FxAPOM is now able to handle tests written using both Selenium WebDriver and Marionette.
Based on the type of driver being used, the package will automatically handle the tests in the way
best suited for that driver including all error handling.

Example of creating an account on the development environment, using the default:

.. code-block:: python

  from fxapom.fxapom import FxATestAccount
  account = FxATestAccount()


Example of creating an account on the development environment, specifying the ``DEV_URL``:

.. code-block:: python

  from fxapom.fxapom import DEV_URL, FxATestAccount
  account = FxATestAccount(DEV_URL)

To sign in via Firefox Accounts, use the ``sign_in`` method in the ``WebDriverFxA`` object,
passing in the email address and password:

.. code-block:: python

  from fxapom.fxapom import WebDriverFxA
  fxa = WebDriverFxA(driver)
  fxa.sign_in(email_address, password)

Note that we are passing ``driver`` into the constructor of ``WebDriverFxA``,
which it then uses to interact with the Firefox Accounts web pages. This driver will
be identified as either an instance of Selenium or Marionette and the tests will be
handled accordingly.

To create an account and then use it to sign in, use both tools described above:

.. code-block:: python

  from fxapom.fxapom import FxATestAccount, WebDriverFxA
  account = FxATestAccount()
  fxa = WebDriverFxA(driver)
  fxa.sign_in(account.email, account.password)

Running The Tests
-----------------

* `Install Tox <http://tox.readthedocs.io/en/latest/install.html>`_
* Run ``tox``

Resources
---------

- `Release Notes <http://github.com/mozilla/fxapom/blob/master/CHANGES.rst>`_
- `Issue Tracker <http://github.com/mozilla/fxapom/issues>`_
- `Code <http://github.com/mozilla/fxapom/>`_
