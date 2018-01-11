Firefox Accounts Page Object Model
==================================

`Selenium WebDriver <http://docs.seleniumhq.org/docs/03_webdriver.jsp>`_
compatible page-object model and utilities for
`Firefox Accounts <https://accounts.firefox.com>`_

.. image:: https://img.shields.io/pypi/l/fxapom.svg
   :target: https://github.com/mozilla/fxapom/blob/master/LICENSE.txt
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
.. image:: https://pyup.io/repos/github/mozilla/fxapom/shield.svg
   :target: https://pyup.io/repos/github/mozilla/fxapom/
   :alt: Updates
.. image:: https://pyup.io/repos/github/mozilla/fxapom/python-3-shield.svg
   :target: https://pyup.io/repos/github/mozilla/fxapom/
   :alt: Python 3

Overview
--------

This package contains a utility to create a test Firefox Account on either the
dev or prod instance of Firefox Accounts, as well as a set of page objects that
can be used to interact with Firefox Accounts' sign in screens.

Installation
------------

To install FxAPOM:

.. code-block:: bash

  $ pip install fxapom

Usage
-----

To create a test Firefox Account, simply create an instance of the
``FxATestAccount`` object. You can pass the url for the Firefox Accounts API
server into the constructor or, if you know you want to create a development
Account, you can omit that argument.

There are two constants available to you to specify the url for either the
development environment or the production environment, which are:

* ``fxapom.DEV_URL`` - the url for the development environment
* ``fxapom.PROD_URL`` - the url for the production environment

Example of creating an account on the development environment, using the
default:

.. code-block:: python

  from fxapom.fxapom import FxATestAccount
  account = FxATestAccount()

Example of creating an account on the development environment, specifying the
``DEV_URL``:

.. code-block:: python

  from fxapom.fxapom import DEV_URL, FxATestAccount
  account = FxATestAccount(DEV_URL)

To sign in via Firefox Accounts, use the ``sign_in`` method in the
``WebDriverFxA`` object, passing in the email address and password:

.. code-block:: python

  from fxapom.fxapom import WebDriverFxA
  fxa = WebDriverFxA(selenium)
  fxa.sign_in(email_address, password)

Note that we are passing ``selenium`` into the constructor of ``WebDriverFxA``,
which it then uses to interact with the Firefox Accounts web pages.

To create an account and then use it to sign in, use both tools described
above:

.. code-block:: python

  from fxapom.fxapom import FxATestAccount, WebDriverFxA
  account = FxATestAccount()
  fxa = WebDriverFxA(selenium)
  fxa.sign_in(account.email, account.password)

Contributing
------------

Fork the repository and submit PRs with bug fixes and enhancements,
contributions are very welcome. You can run the tests using
`Docker <https://www.docker.com/>`_:

.. code-block:: bash

  $ docker build -t fxapom .
  $ docker run -it fxapom tox

Resources
---------

- `Release Notes <http://github.com/mozilla/fxapom/blob/master/CHANGES.rst>`_
- `Issue Tracker <http://github.com/mozilla/fxapom/issues>`_
- `Code <http://github.com/mozilla/fxapom/>`_
