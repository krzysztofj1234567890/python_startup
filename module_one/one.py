import logging
import math

logger = logging.getLogger(__name__)

class Circle:
    def __init__(self, radius: float) -> None:
        if radius < 0:
            logger.error('Invalid radius')
            raise ValueError('The radius cannot be negative')
        self._radius = radius

    def area(self) -> float:
        logger.info("Area calculation")
        return math.pi * math.pow(self._radius, 2)

    def colorPrice(self, color: str) -> int:
        logger.info("Color price calculation")
        return 1