try:
    from pyspark import SparkContext, SparkConf 
    from operator import add
except Exception as e:
    print(e)
def get_counts():
    # That is my example of word counting
    words = "can you can a can as a canner can can a can" 
    # Create a new word count application
    conf = SparkConf().setAppName('word count')
    # Start a new context
    sc = SparkContext(conf=conf)
    # split the words in a list
    seq = words.split()
    # parallelize the list of data
    data = sc.parallelize(seq)
    # Run the count on Spark
    counts = data.map(lambda word: (word, 1)).reduceByKey(add).collect()
    # Stop the count
    sc.stop()
    # Print the results!
    print('\n{0}\n'.format(dict(counts)))
if __name__ == "__main__":
    get_counts()

