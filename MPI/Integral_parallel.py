import random
import matplotlib.pyplot as plt
import numpy as np
from mpi4py import MPI
import numpy as np
import math
import time
import pickle

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


class Function:
    def __init__(self, expression, diapason=(0, 1), function_name='f'):
        self.expression = expression
        self.function_name = function_name
        self.frm, self.to = diapason

    def __call__(self, point=0):
        print('{}({}) = {}'.format(self.function_name, point, self._get_value(point)))

    @property
    def diapason(self):
        return (self.frm, self.to)

    @diapason.setter
    def diapason(self, value):
        self.frm, self.to = value

    def _get_value(self, x):
        return eval(self.expression)

    def _get_segments(self, count=1):
        return np.linspace(self.frm, self.to, count + 1)

    def count_area(self, segments_count=2, processes=1):
        points = self._get_segments(segments_count)
        segments = [[points[p - 1], points[p]] for p in range(1, len(points))]

        if processes == 1:
            sm = 0
            for s in segments:
                sm += self.count_segment(s[0], s[1])
            return sm
        else:
            target_segments = [segments[i] for i in range(len(segments))
                               if i % size == rank]

            part = 0
            for s in target_segments:
                part += self.count_segment(s[0], s[1])

            return part

    def count_segment(self, start, end):
        return (end - start) * (self._get_value(start) + self._get_value(end)) / 2


def measure_time(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()

        if rank == 0:
            # print('{:s} function took {:.3f} ms'.format(f.__name__, (time2-time1)*1000.0))
            file = open("./data/integral_time.txt", "a")
            file.writelines(str(size) + ' ' + str((time2-time1)*1000.0) + '\n')
            file.close()

        return ret
    return wrap


@measure_time
def main():
    '''
        Parallel integral approximation
    '''
    partian_area = f.count_area(segments_count=10000, processes=size)
    result = comm.reduce(partian_area, op=MPI.SUM, root=0)
    if rank == 0:
        # print(result)
        pass


a, b = 5, 7
fexact_solution = math.log(abs(b + math.sqrt(b**2 + 1))) - math.log(abs(a + math.sqrt(a**2 + 1)))

f = Function('1 / math.sqrt(1 + x**2)', diapason=(a, b))


main()




# #####################################################################
# '''
#     Sequential integral approximation
# '''
# partian_area = f.count_area(segments_count=100, processes=1)
# result = comm.reduce(partian_area, op = MPI.SUM, root = 0)
# print(result)
# #####################################################################