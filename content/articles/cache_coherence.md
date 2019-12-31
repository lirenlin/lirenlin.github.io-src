Title: Cache mindmap
Date: Fri 27 Dec 11:30:15 CET 2019
Category: Architecture
Tags: Architecture


# cache hierachy
# cache conflict
## cache miss type, message and action
* write miss
* read miss
* read hit

## inclusive cache, exclusive cache
## write-back, write-through cache
## write-back buffer

# cache coherence protocol

* snoop
* directory

pros vs cons


multi-cycle memory operation, block bus
invalidate copies of all other cache, read from exlucsive/owner cache, change
to share state


store queue
memory model
memory barrier
synchronization
atomic operation

retire, commit, cache visible, store queue
Coherency is maintained by requiring a core to acquire exclusive access to that
cache line before it can modify it (i.e. make a store globally visible by committing it from the store queue to L1D cache).

>
A store buffer is used when writing to an invalid cache line.
Since the write will proceed anyway, the CPU issues a read-invalid message
(hence the cache line in question and all other CPUs' cache lines which store
that memory address are invalidated) and then pushes the write into the store buffer,
to be executed when the cache line finally arrives in the cache.

https://en.wikipedia.org/wiki/MESI_protocol#States


# NUMA


# Ref
https://stackoverflow.com/questions/48974000/are-cache-operations-atomic
https://en.wikipedia.org/wiki/MESI_protocol
https://www.cs.utexas.edu/~bornholt/post/memory-models.html
https://stackoverflow.com/questions/48817022/what-happens-when-different-cpu-cores-write-to-the-same-ram-address-without-sync
https://preshing.com/20120710/memory-barriers-are-like-source-control-operations/
