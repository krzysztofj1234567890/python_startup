import logging
from module_one.one import Circle
from module_one.numpy_data import NumpyData
from module_one.pandas_data import PandasData
from module_one.pyspark_examples import PySparkExamples
from module_one.pyspark_project import KJSparkProject
import sys

# turn on logging
logger = logging.getLogger()
logger.setLevel( logging.DEBUG)

# main
def main():
    # setup handler
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # logger.info('START')
    # logger.info('test circle')
    # circle = Circle(10)
    # logger.info( f"area: {circle.area()}")
    # logger.info( f"color: {circle.colorPrice( 'blue' )}")

    # logger.info('test numpy')
    # numpy_exampes = NumpyData()
    # numpy_exampes.useTypes()
    # numpy_exampes.useRandom()

    # logger.info('test pandas')
    # pandas_exampes = PandasData()
    # pandas_exampes.createDataFrame()

    # logger.info('test pyspark')
    # pyspark_exampes = PySparkExamples()
    # pyspark_exampes.createSession() 
    # pyspark_exampes.createDataFrame() 

    logger.info('===================================>> pyspark project')
    logger.info('===================================>> pyspark project')
    logger.info('===================================>> pyspark project')
    logger.info('===================================>> pyspark project')
    logger.info('===================================>> pyspark project')
    project = KJSparkProject()
    project.run()

    logger.info('END')

if __name__ == '__main__':
    main()