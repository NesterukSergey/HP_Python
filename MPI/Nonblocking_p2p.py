
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = rank

print("rank = %r, data = %r" % (rank, data))

# All processes wait here for all
comm.Barrier()
print("Barrier")
# The same here
# Try to comment one of and both of barriers
comm.Barrier()

# Send, not wait
request = comm.isend(data, dest = (rank + 1) % size)

# Receive, not wait
request = comm.irecv(source = (rank - 1) % size)
# Wait for corresponding sender
data = request.wait()

print("rank = %r, data = %r" % (rank, data))
