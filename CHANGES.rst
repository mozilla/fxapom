Release Notes
-------------

**1.9.0 (2016-07-15)**

* Wait for the sign in page to load when not in a popup

**1.8.0 (2016-05-11)**

* Pulled in PyFxA 0.2.0, to fix mock-import issue

**1.7.2 (2016-05-10)**

* Pulled in latest pyfxa 0.1.3

**1.7.1 (2016-02-09)**

* Fix regressions caused by removing implicit waits and Marionette functionality

**1.7 (2016-02-05)**

* Added `Marionette <https://developer.mozilla.org/en-US/docs/Mozilla/QA/Marionette>`_ functionality

**1.6 (2016-01-19)**

* Remove the requirement to pass ``base_url`` into pages in the page object model.
* Update readme to remove outdated references to ``mozwebqa``.

**1.5 (2015-11-13)**

* Switch the test suite to use ``pytest-selenium``
* Remove implicit waits from the tests and page objects

**1.4 (2015-07-22)**

* Accounts created via ``FxATestAccount`` are now automatically deleted when the object leaves scope
* The ``create_account`` method has been removed from ``FxATestAccount`` as accounts are now automatically created on instantiation
* This is a **breaking change**

**1.3.1 (2015-06-19)**

* Change the README to ``rst`` format

**1.3 (2015-06-18)**

* Change FxATestAccount constructor to accept the url to the FxA API server
* This is a **breaking change**

**1.2 (2015-03-20)**

* Update required version of PyFxA in setup.py to 0.0.5

**1.1 (2015-03-20)**

* Update required version of PyFxA in requirements.txt to 0.0.5

**1.0 (2015-02-20)**

* Initial release
