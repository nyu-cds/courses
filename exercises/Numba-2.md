---
layout: exercise
title: Numba 2
---

Add a vectorized `ufunc` to the `nbody_numba.py` program called `vec_deltas` that takes two NumPy arrays of floats and returns the difference between
each element. For example:

~~~
a = np.arange(0, 3, 1, dtype=np.float64)
b = np.arange(3, 1, -1, dtype=np.float64)
c = vec_deltas(a, b)
~~~
{: .python}

This would result in the array:

~~~
array([-3.0, -1.0, 1.0])
~~~
{: .output}

Modify your `nbody_numba.py` program so that it uses `vec_deltas` rather than the `compute_deltas` function. Hint: This will require making changes
to BODIES so that the first element of each tuple is a NumPy array rather than a list, and the necessary changes to the code in order to support this.

Place the resulting code in `nbody_numba.py` and check that it produces the same results as the original program.

When you are satisfied that your program is working, commit it to the same repository you used in Assignment 3.