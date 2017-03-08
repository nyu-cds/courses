---
layout: exercise
title: Cython 1
---

Use your knowledge of Cython to convert the `nbody_opt.py` program you wrote in Assignment 3 into a Cython program. Pay particular attention
to the following:

* Add `cdef` declarations for all variables
* Use C types in function parameter declarations
* Declare NumPy arrays if you used them, and use efficient indexing

Place the resulting code in a file called `nbody_cython.pyx`. 

Cython provides a module called `pyximport` for importing `.pyx` files directly. This module will load and compile the Cython code automatically
for you. Use the following commands from IPython or Jupyter in order to load the `nbody_cython.pyx` module:

~~~
%load_ext Cython
import pyximport
pyximport.install()
~~~
{: .python}

At this point you should be able to load your Cython program using the normal import statement:

~~~
import nbody_cython
~~~
{: .python}

When you are satisfied that your program is working, commit it to the same repository you used in Assignment 3