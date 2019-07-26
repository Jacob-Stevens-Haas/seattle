# -*- coding: utf-8 -*-
"""
This is a setup.py file.  It allows you to 'install' the package so it can
be imported by python regardless of working directory.  If you're building
an application, a requirements.txt may be more appropriate, as it allows
you to specify the exact dependencies with which your application has
been tested.  On the other hand, if you're building a library that you
want people to use in a variety of places, build a setup.py.  People may
use a library in a variety of projects with other requirements in their
environment, so here we want to specify package requirements as
permissively as possible.'

This file allows you to ship and install the package anywhere.  From
a python interpreter, navigate to the package directory and type
`pip install .`
This will copy the package to the environment's package directory.
Alternatively, we can run
`pip install -e .`
place a symlink from the environment's package directory to wherever
you have this package saved.  Then, when you edit this module, importing
will import the current version of the package.

Resources for more info:
https://python-packaging.readthedocs.io/en/latest/minimal.html
https://packaging.python.org/guides/distributing-packages-using-setuptools/

"""

from setuptools import setup

setup(name='seattle',
      version='0.1.0+untracked',
      description='Helps DS5K grads get better at the software dev side',
      url='https://github.boozallencsn.com/seattle/seattle',
      author='Seattle Data Science Team',
      author_email='stevens-haas_jacob@bah.com',
      license='Internal',
      packages=['numpy', 'pandas', 'xlrd', 'scipy',
                'plotly', 'dash', 'matplotlib'],
      install_requires=['numpy>=1.16', 'pandas>=0.23', 'xlrd>=1.2',
                        'scipy>=1.2','plotly>=4', 'dash>=1.0',
                        'matplotlib>=3.0'],
      zip_safe=False,
      python_requires='~=3.6')
