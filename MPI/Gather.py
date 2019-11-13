
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = rank * rank

print("[Before] rank = %r: data = %r" % (rank, data))

data = comm.gather(data, root = 0)

print("[After] rank = %r: data = %r" % (rank, data))
