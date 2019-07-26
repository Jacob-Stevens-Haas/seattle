# -*- coding: utf-8 -*-
"""
### __init__.py
This is an __init__.py  file.  This file is run whenever the package
is imported.  Names (variables, functions, etc) declared here are
available in the package namespace.  That means that if you start
python, you can type

```
>>> import seattle
>>> print(seattle.city)
```
The interpreter should print
```
Seattle
```
For more guidance on init files, here's a few good references.
* https://stackoverflow.com/questions/448271/what-is-init-py-for
* https://python-packaging.readthedocs.io/en/latest/minimal.html

### Docstrings
This ''' ''' block is a docstring.  It describes what the file does.
Almost all functions, methods, classes, and modules should start with
a docstring.  PEP 257 defines required docstrings.  There's still
some freedom in writing them.  Two major conventions dominate:
numpy style and google style.  We'll use google style.

* Google style guide: http://google.github.io/styleguide/pyguide.html
PEP - Python Enhancement Proposal.  Accepted PEPs become part of
official python rules.
* PEP257 (docstrings):https://www.python.org/dev/peps/pep-0257/
"""

city = 'Seattle'