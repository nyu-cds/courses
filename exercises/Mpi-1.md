---
layout: exercise
title: Message Passing 1
---
Write an MPI program in which the processes with even rank print "Hello" and the processes with odd rank print "Goodbye". Print the rank along with 
the message (for example "Goodbye from process 3"). Hint: remember that although the number of processes is fixed when the program starts, 
the exact number is not known until the `Get_size()` method is called.

Make sure you have adequate comments and documentation in the code, and you follow good software engineering practices.

Call the program `mpi_assignment_1.py` and commit it to the same repository you used for Assignment 3. 
