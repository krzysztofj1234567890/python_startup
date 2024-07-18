import unittest
from pyspark.sql import SparkSession
# from pyspark.testing.utils import assertDataFrameEqual
from module_one.pyspark_examples import PySparkExamples

class PySparkTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spark = SparkSession.builder.appName("Testing PySpark Example").getOrCreate()

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()


class TestPySpark(PySparkTestCase):
    def test_single_space(self):
        sample_data = [{"name": "John    D.", "age": 30},
                       {"name": "Alice   G.", "age": 25},
                       {"name": "Bob  T.", "age": 35},
                       {"name": "Eve   A.", "age": 28}]

        # Create a Spark DataFrame
        original_df = self.spark.createDataFrame(sample_data)

        # Apply the transformation function from before
        examples = PySparkExamples()
        transformed_df = examples.remove_extra_spaces(original_df, "name")

        expected_data = [{"name": "John D.", "age": 30},
        {"name": "Alice G.", "age": 25},
        {"name": "Bob T.", "age": 35},
        {"name": "Eve A.", "age": 28}]

        expected_df = self.spark.createDataFrame(expected_data)

        # assertDataFrameEqual(transformed_df, expected_df)
