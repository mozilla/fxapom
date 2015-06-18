from setuptools import setup, find_packages

# dependencies
deps = ['PyFxA==0.0.6']

setup(name='fxapom',
      version='1.3',
      description="Mozilla Firefox Accounts Page Object Model",
      long_description=open('README.md').read(),
      classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='mozilla',
      author='Mozilla Web QA',
      author_email='mozwebqa@mozilla.org',
      url='https://github.com/mozilla/fxapom',
      license='MPL 2.0',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      install_requires=deps,
      include_package_data=True)
