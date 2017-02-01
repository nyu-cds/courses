---
layout: exercise
title: Version Control 6
---

*These exercises assume that you are working in pairs to add and
 modify files in a common repository. The files are available in the
 [`data`](https://github.com/nyu-cds/courses/tree/master/data) and
 [`code`](https://github.com/nyu-cds/courses/tree/master/code) directories of
 the course repository.*

You're working on a large project trying to predict diversity hotspots. Another
member of your collaborative team has produced a series of files that contain
lists of areas that resulted from a series of modeling exercises. Each filename
begins with the word `areas` and ends with `.txt`. 

You and your team pair decide that everything will be kept in a common repository, and to 
name the repository using a combination of your netIDs and `assignment2`. For example,
if your netIDs are `aaa11` and `bbb22` you would name the repository `aaa11_bbb22_assignment2`.
Since you're going to share a repository, you need to agree on some way to communicate
with each other. You can choose anything you want: email, IM, GitHub Issues, etc.

One team member should create the repository under the `nyu-cds` organization on GitHub. 
Make sure that the second team member has write access  to the repository by choosing 
the `Settings` tab, then  `Collaborators & teams'. Whoever created the repository 
will then need to let their team member know that it is available, and both should 
clone a copy to their computers.

A programmer has whipped up a small python script called `rich_pred.py` that
takes a single file containing a list of areas, one per line, and returns the
area and the predicted richness. The script can be downloaded using the
command `curl -O {{ site.github.url }}/code/rich_pred.py`. 

One team member should download this script and commit it to their local repository, then push the
changes to GitHub using `git push` from the command line. They should then notify the second team member,
who will update their local repository from the command line using `git pull` and
check that they now have a copy of the script.
