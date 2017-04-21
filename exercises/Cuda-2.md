---
layout: exercise
title: CUDA 2
---

Modify your answer above to use shared memory when computing the image array.

~~~
from numba import cuda
import numpy as np

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

    return max_iters

@cuda.jit
def mandel_kernel_shared(min_x, max_x, min_y, max_y, image, iters):
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
mandel_kernel_shared[griddim, blockdim](-2.0, 1.0, -1.0, 1.0, d_image, 20) 
d_image.to_host()
imshow(gimage)
show()
~~~
{: .python}
