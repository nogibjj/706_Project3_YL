from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id

def load(dataset1="dbfs:/FileStore/individual_project3/wc-20140609-140000.csv", 
         dataset2="dbfs:/FileStore/individual_project3/wc-20140613-205820.csv"):
    spark = SparkSession.builder.appName("Read CSV").getOrCreate()

    event_times_df = spark.read.csv(dataset1, header=True, inferSchema=True)
    serve_times_df = spark.read.csv(dataset2, header=True, inferSchema=True)

    event_times_df = event_times_df.withColumn("id", monotonically_increasing_id())
    serve_times_df = serve_times_df.withColumn("id", monotonically_increasing_id())

    serve_times_df.write.format("delta").mode("overwrite").saveAsTable("wc609_delta")
    event_times_df.write.format("delta").mode("overwrite").saveAsTable("wc613_delta")
    
    num_rows = serve_times_df.count()
    print(num_rows)
    num_rows = event_times_df.count()
    print(num_rows)
    
    return "finished transform and load"

if __name__ == "__main__":
    load()