---
layout: exercise
title: Message Passing 3
---
Write a sorting program which works in parallel with collective communication using `mpi4py` for an arbitrary number of processes. The root process 
should generate a large unsorted data set (e.g. 10,000 elements), then slice it into bins by value and send each bin (except one) to the other 
processes to sort. You can utilize any appropriate method to sort the data. The sorted data should then be sent back to the root process and put 
into rank order. The data should now be completely sorted.
    
As an example, consider sorting this data set on four processors:
    
 3 5 7 4 6 7 11 9 2 8 3 2
    
The first (root) process looks at the range of these data and divides it into four groups, one for each process rank. So process with rank 0 will
be sent data in the range 0–2, process 1 will be sent data in the range 3–5, process 2 will be sent data in the range 6–8, and process 3 will be sent
data in the range 9–11:
    
Rank  |  1 | 1 | 2 | 1 | 2 | 2 | 3 | 3 | 0 | 2 | 1 | 0
Data  |  3 | 5 | 7 | 4 | 6 | 7 |11 | 9 | 2 | 8 | 3 | 2
    
Thus process rank 0 receives two data points, `[2, 2]`, while process rank 2 receives four, `[7, 6, 7, 8]`, etc. (A better algorithm will 
balance the load better but that's not your concern right now.)  When each process has sorted its own data points, then reunifying them on 
root will produce a completely sorted data set.
    
Rank  |  0  0 | 1  1  1  1 | 2  2  2  2 | 3  3
Data  |  2  2 | 3  3  4  5 | 6  7  7  8 | 9 11
        
The program must be well structured and follow good software engineering design principles. It must be adequately documented and include tests that 
verify the key components of the program. Call the program `parallel_sorter.py` and place it in an `assignment11` directory along with the test code. 
Commit the directory to the same repository you used for Assignment 3. 
