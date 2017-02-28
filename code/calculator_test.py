# -----------------------------------------------------------------------------
# calculator_test.py
# ----------------------------------------------------------------------------- 
import numpy as np
import calculator as calc

M = 10**3
N = 10**3

A = np.random.random((M,N))
B = np.random.random((M,N))

calc.hypotenuse(A,B)