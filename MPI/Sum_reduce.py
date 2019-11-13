
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Python objects sum-reduce
result = comm.reduce(rank, op = MPI.SUM, root = 0)

if rank == 0:
    print("result = %r" % result)

# Numpy objects sum-reduce
sendbuf = np.empty(2, dtype = 'i')
sendbuf[0] = 1
sendbuf[1] = rank

if rank == 0:
    recvbuf = np.empty(2, dtype = 'i')
else:
    recvbuf = None

comm.Reduce(sendbuf, recvbuf, op = MPI.SUM, root = 0)

if rank == 0:
    print("recvbuf = %r" % recvbuf)
