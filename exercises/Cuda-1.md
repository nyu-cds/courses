---
layout: exercise
title: CUDA 1
---

The following program is the familar computation of the [Mandelbrot set](https://en.wikipedia.org/wiki/Mandelbrot_set).

~~~
#
# Simple Python program to calculate elements in the Mandelbrot set.
#
import numpy as np
from pylab import imshow, show

def mandel(x, y, max_iters):
    '''
    Given the real and imaginary parts of a complex number,
    determine if it is a candidate for membership in the 
    Mandelbrot set given a fixed number of iterations.
    '''
    c = complex(x, y)
    z = 0.0j
    for i in range(max_iters):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i
            
    return max_iters
    
def compute_mandel(min_x, max_x, min_y, max_y, image, iters):
	'''
	Calculate the mandel value for each element in the 
	image array. The real and imag variables contain a 
	value for each element of the complex space defined 
	by the X and Y boundaries (min_x, max_x) and 
	(min_y, max_y).
	'''
    height = image.shape[0]
    width = image.shape[1]
    
    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height
    
    for x in range(width):
        real = min_x + x * pixel_size_x
        for y in range(height):
            imag = min_y + y * pixel_size_y
            image[y, x] = mandel(real, imag, iters)
            
if __name__ == '__main__':
	image = np.zeros((1024, 1536), dtype = np.uint8)
	compute_mandel(-2.0, 1.0, -1.0, 1.0, image, 20) 
	imshow(image)
	show()
~~~
{: .python}

The program works as follows:
1. First, the `image` array is created with shape (1024, 1536) and initialized with zeros.
2. The `compute_mandel` function is called which assigns a value in the range 0 to 19 (`max_iters` - 1) to each element of the array.
3. The array is then plotted.

The `compute_mandel` function assigns a value to each element of the image array by:
1. First calculating `pixel_size_x` and `pixel_size_y`. These correspond to the smallest increments that 
can be represented by each element (or pixel) of the array in the ranges `min_x` .. `max_x` and `min_y` .. `max_y`respectively.
2. Iterating over each element of the array, and computing the `mandel` value that corresponds to the (`real`, `imag`) value of that element. `real`
and `imag` are used because you can think of the X and Y axes as the real and imaginary components of complex numbers.

The `mandel` function works by testing how rapidly the function `z = z*z + c` converges or diverges for a given value of `c = complex(x,y)`.
The value returned is the number of iterations (up to `max_iters`) it takes for the real and imaginary parts of `z` to reach the value 2 (no value
greater than 2 can be part of the set). Faster divergence will result in a smaller number, slower divergence a larger number. A value within the
set will return `max_iters`.

Try running this program to make sure you are familiar with how it works.

You are going to modify this program to work on a GPU using CUDA. You're going to use the same `mandel` function, except that for it to be usable
with a CUDA kernel, you need to add the `@cuda.jit(device=True)` decorator. This tells CUDA that `mandel` is a *device function*, which is a function
that can only be executed by a kernel on the device. You also need to add the `@cuda.jit` decorator to the `compute_mandel` function as this is going to 
become the CUDA kernel.

Finally, you need to modify the `compute_mandel` function so that it can be used as a CUDA kernel. Remember that instead of iterating over every
element of the array, your kernel will need to iterate over a smaller block of elements. The kernel will need to obtain the starting `x` and `y` 
coordinates using `cuda.grid()` and then calculate the ending `x` and `y` coordinates by obtaining the size of the block using `gridDim` and `blockDim`. 
Once you have the starting and finishing `x` and `y` coordinates, you can compute the mandel value for each element of the block as before. 

The final program should look like this (use `mandelbrot_gpu.py` for the file name):

~~~
# 
# A CUDA version to calculate the Mandelbrot set
#
from numba import cuda
import numpy as np
from pylab import imshow, show

@cuda.jit(device=True)
def mandel(x, y, max_iters):
    '''
    Given the real and imaginary parts of a complex number,
    determine if it is a candidate for membership in the 
    Mandelbrot set given a fixed number of iterations.
    '''
    c = complex(x, y)
    z = 0.0j
    for i in range(max_iters):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i

    return max_iters

@cuda.jit
def compute_mandel(min_x, max_x, min_y, max_y, image, iters):
	'''
	YOUR COMMENT HERE
	'''
    ### YOUR CODE HERE
    
if __name__ == '__main__':
	image = np.zeros((1024, 1536), dtype = np.uint8)
	blockdim = (32, 8)
	griddim = (32, 16)
	
	image_global_mem = cuda.to_device(image)
	compute_mandel[griddim, blockdim](-2.0, 1.0, -1.0, 1.0, image_global_mem, 20) 
	image_global_mem.copy_to_host()
	imshow(image)
	show()
~~~
{: .python}

You need to replace `### YOUR CODE HERE` with your code. In addition, it is *essential* that you replace `YOUR COMMENT HERE` with a comment describing 
how your code works.

When you are satisfied it works correctly, commit `mandelbrot_gpu.py` to the same repository you used in Assignment 3.

Note: don't expect the code to run any faster unless you're running on a real GPU.

