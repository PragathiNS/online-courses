Quiz:
**1. When specifying the `--fork` argument to mongod, what must also be specified?**
- [ ] logfile
- [ ] logdestination
- [ ] loglocation
- [x] logpath

**2. Sharded clusters are composed of:**
- [x] Mongos
- [ ] Load Balancer
- [x] Config Servers
- [x] Replica Sets

**3. Which of the following is true about indexes?**
- [ ] By default, MongoDB doesn't create any indexes.
- [x] Indexes take up space in memory.
- [x] Indexes speed up our read operations.
- [ ] Indexes speed up our write operations.

**4. Consider the following:
`mongod --dbpath /data/db --logpath /data/logs --replSet M103 --bind_ip '127.0.0.1,192.168.0.100' --keyFile /data/keyfile --fork`
Which of the following represents a configuration file equivalent to the command line options?**
- [ ] 
  ```json
  storage
      dbPath="/data/db"
   systemLog
      destination="/data/logs"
   replication
      replSetName="M103"
   net
      bindIp="127.0.0.1,192.168.0.100"
   security
      keyFile="/data/keyfile"
   processManagement
      fork=true
  ```
- [x] 
  ```json
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
  ```
- [ ]
  ```json
  storage.dbPath: /data/db
  systemLog.destination: "/data/logs"
  replication.replSetName: "M103"
  net.bindIp: "127.0.0.1,192.168.0.100"
  security.keyFile: "/data/keyfile"
  processManagement.fork: true
  ```
**5. Which of the following files in the MongoDB data directory can you access to view collection data?**
- [ ] The collection.wt file
- [ ] The storage.bson file
- [ ] The WiredTiger.wt file
- [x] None of the above

**6. Which of the following methods executes a database command?**
- [x] db.runCommand({<COMMAND>})
- [ ] db.runThisCommand({<COMMAND>})
- [ ] db.executeCommand({<COMMAND>})
- [ ] db.command({<COMMAND>})

**7. Which of the following process logging components will capture the following operation, assuming a verbosity of 1 or greater?**
```json
db.runCommand(
  {
    update : "products",
    updates: [
    {
      q: <query>,
      u: <update,
    }
    ]
  }
  )
```
- [x] WRITE
- [ ] QUERY
- [ ] UPDATE
- [x] COMMAND

**8. What events are captured by the profiler?**
- [x] CRUD operations
- [x] Cluster configuration operations
- [x] Administrative commands
- [ ] WiredTiger storage data
- [ ] Network timeouts

**9. When should you deploy a MongoDB deployment with security enabled?**
- [x] When deploying your production environment
- [x] When deploying an evaluation environment
- [x] When deploying your staging environment
- [x] When deploying a development environment

**10. Which of the following are Built-in Roles in MongoDB?**
- [x] dbAdminAnyDatabase
- [x] read
- [ ] dbAdminAllDatabases
- [ ] readWriteUpdate
- [ ] rootAll

**11. Which of the following are true differences between mongoexport and mongodump?**
- [ ] Mongoexport outputs BSON, but mongodump outputs JSON.
- [x] Mongodump can create a data file and a metadata file, but mongoexport just creates a data file.
- [x] Mongodump outputs BSON, but mongoexport outputs JSON.
- [ ] Mongoexport is typically faster than mongodump.
- [x] By default, mongoexport sends output to standard output, but mongodump writes to a file.
