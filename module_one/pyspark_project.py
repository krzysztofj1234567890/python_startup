from pyspark.sql import SparkSession
from pyspark.sql import Row

# first run:
# docker run -p 7077:7077 -p8080:8080 bitnami/spark:3.5.1


# class KJSparkProject:
#     def run(self):
#         spark = SparkSession.builder \
#             .appName("PySpark Project") \
#             .master("spark://127.0.0.1:7077") \
#             .getOrCreate()
#         df = spark.createDataFrame([
#             Row(a=1, b=2., c='string1' ),
#             Row(a=2, b=3., c='string2' ),
#             Row(a=4, b=5., c='string3' )
#         ])
#         df.printSchema()

class KJSparkProject:
    def run(self):
        # create spark session
        spark = SparkSession.builder \
            .appName("PySpark project") \
            .master("spark://192.168.177.1:7077") \
            .getOrCreate()

        # load file
        # dataframe = spark.read.format('csv')\
        #         .option('header','true')\
        #         .option('inferSchema', 'true')\
        #         .option('timestamp', 'true')\
        #         .load('data/small_set.csv')
        
        dataframe = spark.createDataFrame([
                Row(a=1, b=2., c='string1' ),
                Row(a=2, b=3., c='string2' ),
                Row(a=4, b=5., c='string3' )
            ])

        # show
        dataframe.show()

        # count
        dataframe.count()

        # select
        spark.sql( "SELECT * FROM dataframe" ).collect()

        dataframe.printSchema()


