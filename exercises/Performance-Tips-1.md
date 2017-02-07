---
layout: exercise
title: Performance Tips 1
---

An astrophysicist colleague was recently complaining about how long it was taking to run an N-body simulation. 
"It's really just a simple calculation, and I'm only simulating four planets, but it takes nearly a minute and
a half to run one simulation. I really need it done in under 30 seconds." You kindly offer to take a look at
code to see if it is possible to speed it up. Your colleague provides you with a 
[link to the source]({{ site.github.url }}/code/nbody.py).

Although your colleague said the code was simple, it is still fairly complex, so you decide to tackle the problem
in stages. A first scan of the code reveals a number of potential areas that could be improved. These include:

* Reducing function call overhead
* Using alternatives to membership testing of lists
* Using local rather than global variables
* Using data aggregation to reduce loop overheads

As you're a cautious programmer, you decide to address each of these in turn. This will ensure that
it is possible to check the program is still working correctly after each change, and to assess the performance
improvement that the change achieved. You are also aware that the program has to be maintained by others in the future,
so you want to make sure that the changes do not make this more difficult, especially if the performance improvement
is only minor.

For each of these areas, create a new version of `nbody.py` (call them `nbody_1.py`, `nbody_2.py`, etc.) and commit
them to the repository. You may also add a file with any other optimizations that you find. At the beginning of each 
file, put a comment indicating if the change made the most improvement, second most, etc. Finally, create another 
file called `nbody_opt.py` that contains all of the optimizations you made.
Put a comment at the top indicating the relative speedup of the optimized version compared to the original version. 
Calculate the relative speedup (R) as follows:

![]({{ site.github.url }}/public/speedup_1.png

where

![]({{ site.github.url }}/public/speedup_2.png
![]({{ site.github.url }}/public/speedup_3.png
 
Are you able to get it to run in under 30 seconds?
