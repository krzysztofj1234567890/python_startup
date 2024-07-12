import logging
import pandas 

logger = logging.getLogger(__name__)

class PandasData:
    def createDataFrame(self):
        cities = {"name": ["London", "Berlin", "Madrid", "Rome",
                    "Paris", "Vienna", "Bucharest", "Hamburg",
                    "Budapest", "Warsaw", "Barcelona",
                    "Munich", "Milan"],
                "population": [8615246, 3562166, 3165235, 2874038,
                    2273305, 1805681, 1803425, 1760433,
                    1754000, 1740119, 1602386, 1493900,
                    1350680],
                "country": ["England", "Germany", "Spain", "Italy",
                    "France", "Austria", "Romania",
                    "Germany", "Hungary", "Poland", "Spain",
                    "Germany", "Italy"]}
        city_frame = pandas.DataFrame(cities)
        logger.info( city_frame )
        logger.info( "sum" )
        logger.info( city_frame.sum() )
        logger.info( "sort" )
        logger.info( city_frame.sort_values(by="population", ascending=False) )
        logger.info( "group by" )
        logger.info( city_frame.groupby(["country"]).sum() )