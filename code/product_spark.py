#
# Calculate the product of the integers between 1 and 1000 inclusive using Spark
#
from pyspark import SparkContext

if __name__ == '__main__':
    sc = SparkContext("local", "product_spark");

    # Create an RDD containing the numbers 1 to 1000 inclusive
    nums = sc.parallelize(range(1, 1001))

    # Apply the lambda to the first two elements, then the result and the next element, and so on...
    # Accumulates the product of all the elements.
    mult = nums.fold(1, (lambda x, y: x * y))

    # Print the result
    print(mult)