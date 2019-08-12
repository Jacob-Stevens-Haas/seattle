#Auto Documentation How-To

Everything in this folder is automatically generated, other than this file
and index.html.  To port this to a new project, once sphinx is pip-installed,
just copy make.bat, Makefile, index.html, source/conf.py into your docs/ folder.  

If you want to start from scratch, however, here's the instructions for 
setting up automatic documentation for your project.  It's ~~pretty hard~~
a simple 17-step process requiring guaranteed troubleshooting.  If
anything differs from the steps you take or the structure of your project,
you'll have to spend quite some time troubleshooting how to get it right.
You may have to spend a lot of time getting familiar with `git push --force`,
 `git reset`, and `git revert`.  Also note that documentation online often
 applies to sphinx pre-2.0, which gave a lot more options for
 `sphinx-quickstart`.

1. Enter project directory
2. enter virtual environment
3. If not already installed, pip install sphinx and sphinxcontrib.napoleon
4. `mkdir docs`
5. `cd docs`
6. `sphinx-quickstart` (choose 'yes' to separate source and build directories).
This will add a Makefile and a make.bat file here, as well as source/ and 
build/ directories.
7. In `source/index.rst`, add `   modules` under the toctree, so it looks like:
```
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules
```
Be careful now children.  That's a three-space indent before modules.  If you
hit the tab key, you lose.  
8. If your package is deep, change maxdepth to a bigger number.  
9. Add extensions to `source/conf.py`.  Open the file, and change line 33 to
```
extensions = ['sphinx.ext.autodoc', #Allows sphinx-apidoc to work right
            'sphinx.ext.todo', #allows inline "To Do:" blocks. Optional
            'sphinx.ext.imgmath', #Allows LaTeX equations in .rst files. Optional
            'sphinx.ext.napoleon', #Allows google and numpy style docstrings
            'sphinx.ext.githubpages', #Adds .nojekyll file to make it work
]
```
10. If you did not pip install the seattle package, uncomment the lines:
```
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
```
Change '.' to navigate from the docs/ folder to your package folder (likely '..')  
11. Add `sphinx-apidoc -f -e -o source ../seattle` to make.bat after `@echo off`.  If
you add other files that you don't yet want to document, add their path from docs/
to the end of the command, separating them with commas if more than one excluded
file.  Wildcards (e.g. ?, * [include] [!exclude]) are allowed in the path (For windows,
at least. If on Unix/Linux/Mac, add this command somewhere at the beginning of the 
Makefile.

sphinx-apidoc is a program that turns python packages into reStructured text files
(.rst).  sphinx-build, which you also see in make.bat, then turns the rst files into 
html, pdf, or other formats.  This command differs takes two arguments: where to 
put rst files, and where to find python files.  
12. `make html`  
If you get build errors, try to google them to figure out what you should change.
Ask for help. The google group tends to be pretty responsive.
13. Check your highest-level .gitignore file for `source/` and `build/` and remove
them if they are present (or add an exception for `docs/source` and `docs/build`).  
14. Create a file `index.html` in docs/.  As the only line, it should have:
```
<meta http-equiv="refresh" content="0; url=./build/html/index.html" />
```
GitHub pages looks for an index.html file at the top of your docs/ folder.  Just
have it redirect to docs/build/html/index.html.  
15. Verify that you have a `docs/.nojekyll` file.  It should be empty.  
16. Push your changes to GitHub and merge with master  
17. Go to the settings tab on your github repo and enable Github Pages from the 
master/docs folder.
