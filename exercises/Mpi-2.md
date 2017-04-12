---
layout: exercise
title: Message Passing 2
---
Write an MPI program that does the following for some arbitrary number of processes:

Process 0 reads a value from the user and verifies that it is an integer less than 100.
Process 0 sends the value to process 1 which multiplies it by its rank.
Process 1 sends the new value to process 2 which multiplies it by its rank.
This continues for each process, such that process `i` sends the value to process `i+1` which multiplies it by `i+1`.
The last process sends the value back to process 0, which prints the result.

You can use either blocking or non-blocking operations. An input read from the user must be validated correctly. Make sure you have 
adequate comments and documentation in the code, and you follow good software engineering practices.

Call the program `mpi_assignment_2.py` and commit it to the same repository you used for Assignment 3. 


