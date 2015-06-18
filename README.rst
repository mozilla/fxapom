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

Usage
-----

To create a test Firefox Account, use the ``create_account`` method in the ``FxATestAccount`` object.
You can pass the url for the Firefox Accounts API server into the constructor
or, if you know you want to create a development Account, you can omit that argument.

There are two constants available to you to specify the url for either the development environment
or the production environment, which are:

* ``fxapom.DEV_URL`` - the url for the development environment
* ``fxapom.PROD_URL`` - the url for the production environment

Example of creating an account on the development environment, using the default:

.. code-block:: python

  from fxapom.fxapom import FxATestAccount
  acct = FxATestAccount().create_account()


Example of creating an account on the development environment, specifying the ``DEV_URL``:

.. code-block:: python

  from fxapom.fxapom import DEV_URL, FxATestAccount
  acct = FxATestAccount(DEV_URL).create_account()

To sign in via Firefox Accounts, use the ``sign_in`` method in the ``WebDriverFxA`` object,
passing in the email address and password:

.. code-block:: python

  from fxapom.fxapom import WebDriverFxA
  fxa = WebDriverFxA(mozwebqa)
  fxa.sign_in(email_address, password)

Note that we are passing ``mozwebqa`` into the constructor of ``WebDriverFxA``, which is only
generally available when using our in-house plugin `pytest-mozwebqa <https://github.com/mozilla/pytest-mozwebqa>`_.

To create an account and then use it to sign in, use both tools described above:

.. code-block:: python

  from fxapom.fxapom import FxATestAccount, WebDriverFxA
  acct = FxATestAccount().create_account()
  fxa = WebDriverFxA(mozwebqa)
  fxa.sign_in(acct.email, acct.password)

Running The Tests
-----------------

* Install the requirements using `pip install -r requirements.txt`
* Run the tests using a local Firefox browser via `py.test --driver=Firefox tests`

Change Log
----------

1.3.1
^^^^^

* Change the README to `rst` format

1.3
^^^

* Change FxATestAccount constructor to accept the url to the FxA API server
* This is a **breaking change**

1.2
^^^

* Update required version of PyFxA in setup.py to 0.0.5

1.1
^^^

* Update required version of PyFxA in requirements.txt to 0.0.5

1.0
^^^

* Initial release
