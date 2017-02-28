---
layout: exercise
title: Performance Tuning 2
---

A colleage has asked you for help. They have been given a task of developing a calculator program in Python that will be used for a
numerically intensive task. It's important that it works as fast as possible, or the project results may be delayed. Your colleage
has a pretty good understanding of Python, and so developed the program using NumPy to help improve the performance. Unfortunately
it is not working well enough for the project, and they have run out of ideas on how to make it better. You offer to help, since you
recently found out about the `cProfile` and `line_profiler` tools.

Download the [source code]({{ site.github.url }}/code/calculator.py) and [tests]({{ site.github.url }}/code/calculator_test.py) for the program.
Use `cPython` and `line_profiler` to determine where the code is performing poorly and why. Make changes to the code to improve the performance
and add a comment to the top of the `cacluator.py` file to indicate the speedup you achieve. Commit the resulting program to the repository you 
created in Assignment 3. Keep the same name for the program, and only `calculator.py` needs to be committed.