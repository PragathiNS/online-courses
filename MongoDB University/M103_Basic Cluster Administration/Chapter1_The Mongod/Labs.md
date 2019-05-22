### Lab 1 - Launching Mongod


#### Problem:


In this lab, you're going to launch your own mongod with a few basic command line arguments.


Applying what you've learned so far about the mongod process, launch a mongod instance, from the command line, with the following requirements:
```
run on port 27000
data files are stored in /data/db/
listens to connections from the IP address 192.168.103.100 and localhost
authentication is enabled
```
By default, a mongod that enforces authentication but has no configured users only allows connections through the localhost. Use the mongo shell on the Vagrant box to use the localhost exception and connect to this node.


Use the following command to connect to the Mongo shell and create the following user. You will need this user in order to validate subsequent labs.
``` json
mongo admin --host localhost:27000 --eval '
  db.createUser({
    user: "m103-admin",
    pwd: "m103-pass",
    roles: [
      {role: "root", db: "admin"}
    ]
  })
'
```
The above command creates a user with the following credentials:
```
Role: root on admin database
Username: m103-admin
Password: m103-pass
```
When you're finished, run the following validation script in your vagrant and outside the mongo shell and enter the validation key you receive below. If you receive an error, it should give you some idea of what went wrong.

`vagrant@m103:~$ validate_lab_launch_mongod`

Hint: You want to make sure all applicable command line options are set! Also, in case you need to restart the mongod daemon, you may need to kill the process using it's pid.


You can use the following command to find the pid of the process:

`ps -ef | grep mongod`

To kill the process, you can use this command:

`kill <pid>`
