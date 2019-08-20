# -*- coding: utf-8 -*-
"""
This is a setup.py file.  It allows you to 'install' packages from a
distribution so they can be imported by any python environment,
regardless of working directory.

If users (including you) of your distribution are using your work within
python, it can be helpful to organize your work in packages.  At the
risk of oversimplifying, packages are directories that you install.
Installing a package tells python where it's module's are located.
Modules are individual python files.  You can import
packages too, but then you're really just importing the package's
 __init__ module.

Since people may use a package in a variety of projects with unique
requirements, setup.py should specify package requirements as
permissively as possible.'

If you're building a standalone application, a requirements.txt or
enviornment.yml may be more appropriate, as they typically enforce
the exact dependencies with which your application has been tested.
In that case, users can recreate the exact environment for running
your application that you use.


A setup.py file allows you to ship and install the package anywhere.
From the command line, navigate to the package directory and type
`pip install .`
This will copy the package to the environment's package directory.
Alternatively, we can run
`pip install -e .`
The editable (-e) flag allows you edit this module's source code, and
importing the module will always include the most recent saved version.

When distributing a new version of your software, make sure to:
* update your requirements.txt and/or your environment.yml
* make new documentation with`docs/make html`
* update the version info in this file according to 
`semver<https://semver.org/>`
 

Resources for more info:
https://python-packaging.readthedocs.io/en/latest/minimal.html
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://docs.python.org/3.7/distutils/setupscript.html
"""

from setuptools import setup

setup(name='seattle',
      version='0.1.0-beta.3',
      description='Helps DS5K grads get better at the software dev side',
      url='https://github.boozallencsn.com/seattle/seattle',
      author='Seattle Data Science Team',
      author_email='stevens-haas_jacob@bah.com',
      license='Internal',
      packages=['seattle'], # Packages & subpackages for the directory
                              # containintby setup.py
      py_modules=['needle', 'utils', 'app'], #This package's modules
      install_requires=['numpy(>=1.16)', 'pandas(>=0.23)', 'xlrd(>=1.2)',
                        'scipy(>=1.2)','plotly(>=3.0)', 'dash',
                        'matplotlib(>=3.0)'],
      zip_safe=False,
      python_requires='~=3.6')
