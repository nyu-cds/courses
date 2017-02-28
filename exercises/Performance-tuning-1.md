---
layout: exercise
title: Performance Tuning 1
---

Due to the dynamic typing of Python, loops tend to be the most inefficient part of Python programs. Use `cPython` and `line_profiling` to 
locate the functions and lines where the most time is being spent in the `nbody_iter.py` program you wrote for Assignment 5. Use NumPy to
replace the high overhead loops with array operations in order to show a measurable improvement in the performance. Place a comment at the
start of the program indicating the performance improvement you achieved. Call the resulting program `nbody_numpy.py` and commit it to
the same repository.