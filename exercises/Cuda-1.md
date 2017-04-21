---
layout: exercise
title: CUDA 1
---

The following program is the familar computation of the Mandelbrot fractal.

~~~
import numpy as np
from pylab import imshow, show

def mandel(x, y, max_iters):
    """
    Given the real and imaginary parts of a complex number,
    determine if it is a candidate for membership in the Mandelbrot
    set given a fixed number of iterations.
    """
    c = complex(x, y)
    z = 0.0j
    for i in range(max_iters):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i

    return max_iters

def compute_mandel(min_x, max_x, min_y, max_y, image, iters):
    height = image.shape[0]
    width = image.shape[1]

    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height
    
    for x in range(width):
        real = min_x + x * pixel_size_x
        for y in range(height):
            imag = min_y + y * pixel_size_y
            image[y, x] = mandel(real, imag, iters)
            
image = np.zeros((1024, 1536), dtype = np.uint8)
compute_mandel(-2.0, 1.0, -1.0, 1.0, image, 20) 
imshow(image)
show()
~~~
{: .python}

First, modify the above code to implement the `mandel_kernel` function below. Hint: every thread should compute one value of the image array.

~~~
from numba import cuda
import numpy as np
​
@cuda.jit
def mandel_gpu(x, y, max_iters):
    """
    Given the real and imaginary parts of a complex number,
    determine if it is a candidate for membership in the Mandelbrot
    set given a fixed number of iterations.
    """
    c = complex(x, y)
    z = 0.0j
    for i in range(max_iters):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i
​
    return max_iters
​
@cuda.jit
def mandel_kernel(min_x, max_x, min_y, max_y, image, iters):
    # YOUR CODE HERE
~~~
{: .python}

Verify your code works as expected using the host program below.

~~~
from pylab import imshow, show

gimage = np.zeros((1024, 1536), dtype = np.uint8)
blockdim = (32, 8)
griddim = (32,16)

d_image = cuda.to_device(gimage)
mandel_kernel[griddim, blockdim](-2.0, 1.0, -1.0, 1.0, d_image, 20) 
d_image.to_host()
imshow(gimage)
show()
~~~
{: .python}
