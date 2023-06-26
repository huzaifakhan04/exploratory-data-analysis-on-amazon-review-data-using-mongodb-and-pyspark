#   Importing the necessary libraries/modules.

from pyspark.sql import SparkSession

#   Creating an instance of a SparkSession object and connecting it to MongoDB.

spark=SparkSession \
    .builder \
    .appName("StratifiedSample") \
    .master("local") \
    .config("spark.mongodb.input.uri", "mongodb://localhost:27017/") \
    .config("spark.mongodb.output.uri", "mongodb://localhost:27017/") \
    .config("spark.executor.memory", "8g") \
    .config("spark.driver.memory", "8g") \
    .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:3.0.1") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR") #   Overriding the default log level.

#   Reading the dataset from the MongoDB database as a collection into the Spark DataFrame and extracting a stratified sample
#   of a specified sample size based on the product identification number (ASIN).

database="amazon_review_data"
collection="product_reviews"
size=100_000
sample=spark.read.format("com.mongodb.spark.sql.DefaultSource") \
    .option("uri", "mongodb://localhost:27017/"+database+"."+collection) \
    .option("partitioner", "MongoSinglePartitioner") \
    .option("partitionKey", "asin") \
    .option("pipeline", '''[
                                {
                                    '$match':
                                    {
                                        'asin':
                                        {
                                            '$exists': true
                                        }
                                    }
                                },
                                {
                                    '$sample':
                                    {
                                        'size': '''+str(size)+'''
                                    }
                                }
                            ]''') \
    .load()

print("Stratified sample of "+str(size)+" reviews extracted from the `"+collection+"` collection of the `"+database+"` database successfully!")
sample=sample.toPandas().to_csv("./data/sample.csv", index=False)   #   Saving the sample as a comma-separated values (CSV) file.
print("Stratified sample of "+str(size)+" reviews saved as a comma-separated values (CSV) file successfully!")
spark.stop()    #   Stopping the SparkSession object.