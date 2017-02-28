# -----------------------------------------------------------------------------
# calculator.py
# ----------------------------------------------------------------------------- 
import numpy as np

def add(x,y):
    """
    Add two arrays using a Python loop.
    x and y must be two-dimensional arrays of the same shape.
    """
    m,n = x.shape
    z = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            z[i,j] = x[i,j] + y[i,j]
    return z


def multiply(x,y):
    """
    Multiply two arrays using a Python loop.
    x and y must be two-dimensional arrays of the same shape.
    """
    m,n = x.shape
    z = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            z[i,j] = x[i,j] * y[i,j]
    return z


def sqrt(x):
    """
    Take the square root of the elements of an arrays using a Python loop.
    """
    from math import sqrt
    m,n = x.shape
    z = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            z[i,j] = sqrt(x[i,j])
    return z


def hypotenuse(x,y):
    """
    Return sqrt(x**2 + y**2) for two arrays, a and b.
    x and y must be two-dimensional arrays of the same shape.
    """
    xx = multiply(x,x)
    yy = multiply(y,y)
    zz = add(xx, yy)
    return sqrt(zz)