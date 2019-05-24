### Replication - concept of maintaining multiple copies of your data
- asynchronous, statement based replication because it is Platform independent and allows more flexibility within a replica set

Why do we need?
- Availability of the data even when there is a data loss due to server down

Binary replication
- Binary log (bytes written)
- requires very strict consistency across the replica set.
- same platform, versions of OS, DB etc
- Less data and replication in faster

Statement-based replication
- statements are stored in Op Log (Database, statement)
- secondaries sync their op log with the primary's op log
- MongoDB uses this
- insert statements go through a little transformation


Asynchronous replication protocol - PV1 and PV0
- PV1 [Protocol Version 1] -> default version
- based out of RAFT protocol

Arbiter
- node that holds no data
- can vote in an election working as a tiebreaker between secondaries
- cannot become primary
- usually avoid creating an arbiter node

-Hidden and deplayed nodes

maximum of 50 nodes in a replica set and only 7 can vote in the election
