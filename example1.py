try:
    # Import all the necessary libraries
    from pyspark import SparkContext, SparkConf
    import random
except Exception as e:
     print(e)
# I define a function to filter numbers to positive numbers
def positive(a):
    if a>0:
       return a
# I define a function to filter numbers to even numbers
def even(a): 
    if a%2==0:
       return a
# I define the runit, where I apply the Spark methods
def runit(x,y):
     # First, create a new Spark application
     conf = SparkConf().setAppName('Example1 application')
     # Then, I define a new Spark context 
     sc = SparkContext(conf=conf)
     # Then, I define my first transformation (filter positive numbers)
     # to a list of random numbers within a range(x,y)
     tr1 = sc.parallelize(range(x, y)).filter(positive)
     # Then, I define my second transformation (filter even numbers)
     tr2 = tr1.filter(even)
     # Then, I call an action, that is to count the values filtered from 
     # trasnformation 1 and tranformation 2
     print("Stelios count:",tr2.count())
if __name__ == "__main__":
    runit(-10,10) # Run it for values between -10 and 10

