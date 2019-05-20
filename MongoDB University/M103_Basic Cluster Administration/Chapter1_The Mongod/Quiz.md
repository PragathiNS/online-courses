Quiz:
1. When specifying the --fork argument to mongod, what must also be specified?
--logfile
--logdestination
--loglocation
[x] logpath

2. Sharded clusters are composed of:
[x] Mongos
-- Load Balancer
[x] Config Servers
[x] Replica Sets

3. Which of the following is true about indexes?
-- By default, MongoDB doesn't create any indexes.
[x] Indexes take up space in memory.
[x] Indexes speed up our read operations.
-- Indexes speed up our write operations.

4. Consider the following:
mongod --dbpath /data/db --logpath /data/logs --replSet M103 --bind_ip '127.0.0.1,192.168.0.100' --keyFile /data/keyfile --fork
Which of the following represents a configuration file equivalent to the command line options?
storage:
  dbPath: "/data/db"
systemLog:
  destination: file
  path: "/data/logs"
replication:
  replSetName: "M103"
net:
  bindIp: "127.0.0.1,192.168.0.100"
security:
  keyFile: "/data/keyfile"
processManagement:
  fork: true
