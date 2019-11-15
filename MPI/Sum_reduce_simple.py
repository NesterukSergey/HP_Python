
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

result = comm.reduce(rank, op = MPI.SUM, root = 0)

if rank == 0:
    print("result = %r" % result)

