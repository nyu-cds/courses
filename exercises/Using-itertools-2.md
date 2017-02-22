---
layout: exercise
title: Using Itertools 2
---
Write a program that takes two arguments `n` and `k` and prints all binary strings of length `n` that contain `k` zero bits, one
per line. The program:

* Must be called `binary.py`
* Must use the `itertools` module
* Must provide a function called `zbits(n, k)` that returns a set of strings
* Must contain adequate comments and documentation

Run the following tests to ensure that the program is correct.

~~~
import binary
assert binary.bits(4, 3) == {'0100', '0001', '0010', '1000'}
assert binary.bits(4, 1) == {'0111', '1011', '1101', '1110'}
assert binary.bits(5, 4) == {'00001', '00100', '01000', '10000', '00010'}
~~~
{: .python}

Commit the `binary.py` program to the repository you used for `Assignment 3`.