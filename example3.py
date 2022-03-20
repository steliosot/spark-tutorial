from pyspark.sql import SparkSession
spark = SparkSession \
    .builder \
    .appName("Example3 basic SQL") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
# Load the data
df = spark.read.json("examples/src/main/resources/people.json")
# Displays the content of the DataFrame to stdout (standard output)
df.show()
# Create a new view for the people data
df.createOrReplaceTempView("people")
# Run your query on spark
sqlDF = spark.sql("SELECT * FROM people WHERE age>20")
sqlDF.show()

