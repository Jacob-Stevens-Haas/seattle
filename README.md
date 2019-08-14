# DS5K to Python Data Science Developer
This repository is an example of what a python package or project should include.
It is also a self-guided tour of how to build a maintainable, professional python
code.  To that end, each file includes comments to explain what it is for, how to
modify it, and further resources to improve the reader's understanding.  

We created this project as a launch platform for data science training.  There
are many notebooks to teach you how to use boosted trees or how to display
pretty outputs.  But so much of bad data science involves bad coding, and
so much of good data science requires good code.  We're going to teach data science,
but we'll do it with good code.

We decided to  create a skeleton python distribution with all the bells and
whistles.  We can make data science lessons as branches to the repository,
with packages included in this distribution.  This format would force aspiring
data scientists to use git and interact with python's packaging structure.  
Moreover, it would force trainers to use git and python packaging at a 
higher level of competency.

Not every file is necessary in every project.  Some files may be more useful for 
building a python package (e.g. \_\_init\_\_.py), others for applications (e.g.
requirements.txt).  Regardless, you should be able to use the master branch of this
repo as a starting point for any python project.  

## Why? Your Most Important Client
Sometimes, you want to build a stand-alone application that only you care about.
So you may start with some code, but before long, you want to re-use that code
that parsed some input.  So you copy and paste it where you need it, but later on
your inputs change format.  Now you need to modify both the original parsing code
and the copied one.  But you used it all over the place - can you be sure that
you fixed each copy?

All of sudden, you wish that an earlier incarnation of you had the foresight to 
structure your code better.  And what the hell did you mean when, in a bout
of frustration, you commented "need to unfuck this variable"?  It's completely
unclear how the code that follows manages to unfuck anything.  Since the output
still looks slightly fucked, you change `unfuck(this)` to `str(unfuck(this))`
and hope it doesn't break anything.

Finally you want to share your wonderful project.  You find and replace 'unfuck' with
'fix', because you're a professional and you own a few ties and have a nice pair of
shoes.  Then you ship your code to someone and they say, "I don't get how it works,
but it does cool stuff.  Can you do it with this data?"  The answer is no, not for 
cheap.

Whenever a project takes more than one session of butt in chair, we forget important 
stuff about how it works.  Things like variable names.  Column names in a table.
What the point of this or that function is.  The reality is, we start each session of 
code as a new person.  When you write code, you are ALWAYS writing for the most
important client - a future incarnation of yourself.  That client's time is valuable, 
even if they don't own a tie or a pair of dress shoes.

You've learned the first rule of programming.  If you want to write good code, don't 
write a script or a notebook. Write libraries.  Write packages.

## Installation
1. Set up git from the command line (or GitHub desktop) with your credentials
1. Clone this repository
1. Open Anaconda prompt (Helps to use PowerBroker Admin sometimes)
1. create, activate, and setup a virtual environment (read requirements.txt or environment.yml)
1. Run `pip install -e .` from the project directory.
1. Test that everything is copacetic. `cd test`, then `python -m unittest test/test.py`

## Prerequisites
* A basic knowledge of python (how to import modules, assign variables)
* A basic knowledge of programming (what a loop is, what a function is)
* Familiarity with an IDE (Jupyter doesn't count!)
 
## Self-guided tour order
1. This file
1. .gitignore
1. requirements.txt, environment.yml, and setup.py
1. \_\_init\_\_.py
1. notebooks/example.ipynb
1. Documentation: pages.github.boozallencsn.com/seattle/seattle
1. seattle/utils.py
1. seattle/needle.py
1. test/test.py
1. docs/README.md
1. LICENSE.md
1. CONTRIBUTING.md
1. vis.py

There's no need to look in the data/ and notebooks/ directories, as their contents
are gitignored.

## How to write these .md files
[Good](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf)
[guides](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
