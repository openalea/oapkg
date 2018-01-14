============
Installation
============

For Users
=========

The easiest method is to directly install the package hosted on PyPI::

    $ pip install {{ base.pkgname }}

For Developers
==============

We recommend using a dedicated conda environment when installing a new package,
so create it if you haven't done it already::

    $ conda create -n myenv python

Then activate it::

    $ activate myenv

Download (or clone) the source and then, at the command line::

    (myenv) $ conda env update --file requirements.yml
    (myenv) $ conda env update --file dvlpt_requirements.yml
    (myenv) $ python setup.py develop


If conda fails to install a package, it usually means that one of the required
package cannot be installed with conda. There is three possibilities:

 - the package is developed by the openalea community: follow instruction associated to the package
   that can be found on openalea_
 - the package is an external package: try using pip to install it instead of
   conda.
 - the package is not available on the default channel. You can try using a less
   esoteric package next time :)

.. _openalea: http://virtualplants.github.io/

Run test suite
--------------

 - Use pytest to run all unit tests associated to the package::

    (myenv) $ pytest

   By default, coverage is activated and will list the lines of codes which are
   currently not covered by your tests.

 - Use pytest with the 'runslow' option to run all tests including functional tests
   that may require more time to run::

    (myenv) $ pytest --runslow

Compile documentation on your computer
--------------------------------------

Continuous integration will take care of compiling your documentation automatically
to ensure the web version of the documentation is always accurate. However if you
want to launch sphinx and compile the documentation on your computer for a quick
review purpose for example use the 'build_sphinx' option of 'setup.py'::

    (myenv) $ python setup.py build_sphinx

This will create some files in build/sphinx/html. Open the 'index.html' to access
the main page of the documentation in a browser.