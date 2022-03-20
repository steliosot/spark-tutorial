try:
    from pyspark import SparkContext, SparkConf
    from operator import add
    import random
except Exception as e:
     print(e)
def inside(p):
     x, y = random.random(), random.random()
     return x*x + y*y < 1
def runit(NUM_SAMPLES):
     conf = SparkConf().setAppName('Example 2 pi')
     sc = SparkContext(conf=conf)
     count = sc.parallelize(range(0, NUM_SAMPLES)).filter(inside).count()
     print("Pi is roughly %f" % (4.0 * count / NUM_SAMPLES))
if __name__ == "__main__":
    runit(100)

