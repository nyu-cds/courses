---
layout: exercise
title: BigData 2
---

We saw how to use the `SparkContext.parallelize` method to create a distributed dataset (RDD) containing all the numbers from 0 to 1,000,000. Use this
same method to create an RDD containing the numbers from 1 to 1000. The RDD class has a handy method called 
[fold](https://spark.apache.org/docs/1.1.1/api/python/pyspark.rdd.RDD-class.html#fold) which aggregates all the elements of the data set 
using a function that is supplied as an argument. Use this method to creat a program that
calculates the product of all the numbers from 1 to 1000 and prints the result.

Call your new program `product_spark.py` and commit it to the repository you used for Assignment 3.

