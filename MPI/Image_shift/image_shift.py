import time
import numpy as np


class Map:
    def __init__(self, x_size=100, y_size=100, add_random=False):
        self.__x_size = x_size
        self.__y_size = y_size
        self.__add_random = add_random

        self.__init_map()

    def __init_map(self):
        self.map = np.random.choice([0, 1], (self.__x_size, self.__y_size))


