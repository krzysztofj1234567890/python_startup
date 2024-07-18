from datetime import datetime, date
import logging
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql import Row
from pyspark.sql.functions import col, regexp_replace

logger = logging.getLogger(__name__)

class PySparkExamples:
    def createSession(self):
        logger.info( "create session" )
        spark = SparkSession.builder \
            .appName("Testing PySpark Example 1") \
            .master("spark://127.0.0.1:7077") \
            .getOrCreate()
        
    def createDataFrame(self):
        logger.info( "createDataFrame" )
        spark = SparkSession.builder \
            .appName("Testing PySpark Example 1") \
            .master("spark://127.0.0.1:7077") \
            .getOrCreate()
        df = spark.createDataFrame([
            Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
            Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
            Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
        ])
        logger.info( df )
        df.printSchema()

    # Remove additional spaces in name
    def remove_extra_spaces(self, df, column_name):
        # Remove extra spaces from the specified column
        df_transformed = df.withColumn(column_name, regexp_replace(col(column_name), "\\s+", " "))

        return df_transformed