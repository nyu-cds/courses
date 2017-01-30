---
layout: exercise
title: Version Control 9
---

This is a follow up question to
[Version Control 8](/exercises/Version-control-8).

A colleague emails a team member that some of the parameter values that are being used in `rich_pred.py`
are incorrect and need to be changed urgently. Unfortunately in their haste, the colleague accidentally 
sent an old email to one of the other team members.

The first email said "Please go to the line that
defines `sar_parameters` and change it to

```
sar_parameters = [[22.7, 0.3], [1.2, 0.163, 0.009],
                  [14.36, 21.16], [85.91, 42.57],
				  [1082.45, 1.59, 390000000]]
```
"

The second, incorrect, email said "Please go to the line that
defines `sar_parameters` and change it to

```
sar_parameters = [[22.7, 0.3], [1.2, 0.163, 0.010],
                  [14.36, 21.45], [85.91, 42.57],
				  [1082.45, 1.59, 390000000]]
```
"

Now, follow these instructions carefully:

1.  Each team member should save their version of the file and commit the change to their
    local repository.
2.  Both should try to push the change to the GitHub repository.
3.  One team member should get an error indicating that the commit failed because
    they aren't up to date with the repository (changes have been made since
    they last update).
4.  Pull those changes down, resolve any conflicts, and if necessary commit the correct
    version of the file.
