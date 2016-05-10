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

* Install the requirements using ``pip install -r requirements.txt``
* Run the tests using a local Firefox browser via ``py.test --driver=Firefox tests``

Change Log
----------

1.7.2
^^^^^
* Pulled in latest pyfxa 0.1.3

1.7.1
^^^^^

* Fix regressions caused by removing implicit waits and Marionette functionality

1.7
^^^

* Added `Marionette <https://developer.mozilla.org/en-US/docs/Mozilla/QA/Marionette>`_ functionality

1.6
^^^

* Remove the requirement to pass ``base_url`` into pages in the page object model.
* Update readme to remove outdated references to ``mozwebqa``.

1.5
^^^

* Switch the test suite to use ``pytest-selenium``
* Remove implicit waits from the tests and page objects

1.4
^^^

* Accounts created via ``FxATestAccount`` are now automatically deleted when the object leaves scope
* The ``create_account`` method has been removed from ``FxATestAccount`` as accounts are now automatically created on instantiation
* This is a **breaking change**

1.3.1
^^^^^

* Change the README to ``rst`` format

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
