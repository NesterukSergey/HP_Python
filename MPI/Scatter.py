
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = [x**2 for x in range(comm.Get_size())]
else:
    data = None

print("[Before] rank = %r: data = %r" % (rank, data))

data = comm.scatter(data, root = 0)

print("[After] rank = %r: data = %r" % (rank, data))
