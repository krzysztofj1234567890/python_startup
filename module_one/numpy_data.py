import logging
import numpy 

logger = logging.getLogger(__name__)

class NumpyData:
    def useTypes(self):
        dt = numpy.dtype([('country', 'S20'), ('density', 'i4'), ('area', 'i4'), ('population', 'i4')])
        population_table = numpy.array([
            ('Netherlands', 393, 41526, 16928800),
            ('Belgium', 337, 30510, 11007020),
            ('United Kingdom', 256, 243610, 62262000)],
            dtype=dt)
        logger.info(population_table[:3])

    def useRandom(self):
        x = numpy.random.random_sample((3, 4))
        logger.info( x )