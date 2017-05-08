#
# Calculate the average of the square root of all the numbers between 1 and 1000 inclusive using Spark.
#
from math import sqrt
from pyspark import SparkContext

if __name__ == '__main__':
    sc = SparkContext("local", "squareroot_spark");

    # Create an RDD containing the numbers 1 to 1000 inclusive
    nums = sc.parallelize(range(1, 1001))
    
    # Create an RDD containing the square root of all the numbers
    sqrts = nums.map(lambda x: sqrt(x))
    
    # Create an RDD containing square root counts
    sqrts_map = sqrts.map(lambda x: (x, 1))
    
    # Aggregate sum of square root counts
    sumAndCount = sqrts_map.fold((0, 0), (lambda x, y: (x[0] + y[0], x[1] + y[1])))
    
    # Compute the mean
    print(float(sumAndCount[0]) / float(sumAndCount[1]))