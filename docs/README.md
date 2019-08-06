#Auto Documentation How-To
Everything in this folder is automatically generated, other than this file
and index.html.  To port this to a new project, once sphinx is git-installed,
just copy, Makefile, index.html, source/conf.py into your docs/ folder.  

If you want to start from scratch, however, here's the instructions for 
setting up automatic documentation for your project.  It's pretty hard - if
anything differs from the steps you take or the structure of your project,
you'll have to spend quite some time trouble-shooting how to get it right.
Documentation online often applies to sphinx pre-2.0, which gave a lot more
options for `sphinx-quickstart`

1. Enter project directory
1. enter virtual environment
1. If not already installed, pip install sphinx and sphinxcontrib.napoleon
1. `mkdir docs`
1. `cd docs`
1. `sphinx-quickstart` (choose 'yes' to separate source and build directories).
This will add a Makefile and a make.bat file here, as well as source/ and 
build/ directories.
1. Add extensions to `source/conf.py`.  Open the file, and change line 33 to
```
extensions = ['sphinx.ext.autodoc',
            'sphinx.ext.todo',
            'sphinx.ext.imgmath',
            'sphinx.ext.napoleon',
            'sphinx.ext.githubpages',
]
```
1. If you did not pip install the seattle package, uncomment the lines:
```
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
```
Change '.' to navigate from the docs/ folder to your package folder (likely '..')
1. Add `sphinx-apidoc -f -o source ../seattle` to make.bat after `@echo off`.  If
you add other files that you don't yet want to document, add their path from docs/
to the end of the command, separating them with commas if more than one excluded
file.  Wildcards (e.g. ?, * [include] [!exclude]) are allowed in the path.
If on Unix/Linux/Mac, add this command somewhere at the beginning of the Makefile.
sphinx-apidoc is a program that turns python packages into reStructured text files
(.rst).  sphinx-build, which you also see in make.bat, then turns the rst files into 
html, pdf, or other formats.  This command differs takes two arguments: where to 
put rst files, and where to find python files. 
1. `make html`
If you get build errors, try to google them to figure out what you should change.
Ask for help. The google group tends to be pretty responsive.
1. Create a file `index.html` in docs/.  As the only line, it should have:
```
<meta http-equiv="refresh" content="0; url=./build/html/index.html" />
```
GitHub pages looks for an index.html file at the top of your docs/ folder.  Just
have it redirect to docs/build/html/index.html.  
1. Push your changes to GitHub and merge with master
1. Go to the settings tab on your github repo and enable Github Pages from the 
master/docs folder.
