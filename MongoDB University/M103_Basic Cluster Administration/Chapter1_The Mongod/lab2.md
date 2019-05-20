In this lab, you're going to launch a mongod instance in the vagrant environment with the same exact settings as the previous lab. However this time, those settings will be defined in a configuration file instead of the command line. It is required for this lab that you use the YAML format to construct this config file.

As a reminder, here are the requirements of your mongod instance:

run on port 27000
data files are stored in /data/db/
listens to connections from the IP address 192.168.103.100 and localhost
authentication is enabled
If you created the user from the previous lab, you don't need to create any new users. If you did not create the user, do so now. Here are the requirements for that user:

Role: root on admin database
Username: m103-admin
Password: m103-pass.
When your config file is complete, launch mongod with the --config <config_filepath> command line option with the filepath to your config file in place of config_filepath (you can also use the -f option instead of --config).

When you're finished, run the following validation script in your vagrant and outside the mongo shell and enter the validation key you receive below. If you receive an error, it should give you some idea of what went wrong.

vagrant@m103:~$ validate_lab_configuration_file


ANSWER:
vagrant@m103:~$ mongod --config mongod_custom.conf
about to fork child process, waiting until server is ready for connections.
forked process: 3174
child process started successfully, parent exiting
vagrant@m103:~$ ps -ef | grep mongod
vagrant   3174     1 14 05:52 ?        00:00:00 mongod --config mongod_custom.conf
vagrant   3204  2756  0 05:52 pts/0    00:00:00 grep --color=auto mongod
vagrant@m103:~$ validate_lab_configuration_file
5a2f0e41ae3c4e2f7427ee8f

mongod_custom.conf
# mongod.conf

# for documentation of all options, see:
#   http://docs.mongodb.org/manual/reference/configuration-options/

# Where and how to store data.
storage:
  dbPath: /data/db/
  journal:
    enabled: true
#  engine:
#  mmapv1:
#  wiredTiger:

# where to write logging data.
systemLog:
  destination: file
  logAppend: true
  path: /var/log/mongodb/mongod.log

# network interfaces
net:
  port: 27000
  bindIp: "127.0.0.1,192.168.103.100"


# how the process runs
processManagement:
  timeZoneInfo: /usr/share/zoneinfo
  fork: true

#security:

#operationProfiling:

#replication:

#sharding:

## Enterprise-Only Options:

#auditLog:

#snmp:

security:
  authorization: enabled
