#
# Count the number of distinct words in the input text
#
from pyspark import SparkContext
import re

def splitter(line):
    ''' 
    Split the input line into words and return a list containing 
    lowecase versions of the words.
    '''
    line = re.sub(r'^\W+|\W+$', '', line)
    return map(str.lower, re.split(r'\W+', line))

if __name__ == '__main__':
    sc = SparkContext("local", "distinct_spark")

    # Create an RDD containing the lines of text
    text = sc.textFile('pg2701.txt')

    # Apply the splitter function and return a new RDD containing words
    words = text.flatMap(splitter)
    
    # Map the words into tuples containing the number of occurrences
    words_mapped = words.map(lambda x: (x,1))
    
    # Sort the mapping
    sorted_map = words_mapped.sortByKey()
    
    # Reduce the mapping to count the occurrences of each word, then count the number of elements
    print(sorted_map.reduceByKey(lambda x,y:x).count())