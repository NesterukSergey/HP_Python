
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# In real code this section might read in data from file
if rank == 0:
    size = 10
    comm.send(size, dest = 1)

    data = np.linspace(0.0, 3.14, size)
    comm.Send(data, dest = 1)

    print("Sended data = %r" % data)

elif rank == 1:
    size = comm.recv(source = 0)

    # Allocate space to receive the array
    data = np.empty(size, dtype = 'd')
    comm.Recv(data, source = 0)

    print("Received data = %r" % data)

else:
    data = None

    print("Other data = %r" % data)
