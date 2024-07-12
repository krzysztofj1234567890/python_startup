import logging
from module_one.one import Circle
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

    logger.info('Started')
    circle = Circle(10)
    logger.info( f"area: {circle.area()}")
    logger.info( f"color: {circle.colorPrice( 'blue' )}")
    logger.info('Finished')

if __name__ == '__main__':
    main()