n this lab, you're going to edit the config file from the previous lab to include a different DB path than the default path /data/db. Mongod will now store data files in this new directory instead.

Using what you know about the configuration file and Linux user groups, please complete the following:

create a new folder /var/mongodb/db/ and allow mongod to write files to this directory
create this directory with sudo, because /var is owned by root
use chown to change the owner of this directory to vagrant:vagrant
edit your config file to use this new directory as the dbpath
Here are the updated requirements for your mongod instance:

runs on port 27000
stores its data files in /var/mongodb/db/
listens to connections from the IP address 192.168.103.100 and localhost
uses authentication
Now that your config file has changed, you have to restart mongod so the server will reflect those changes. As a reminder, here is the way to safely shutdown from the mongo shell:

use admin
db.shutdownServer()
quit()
Once your mongod is safely stopped, you can launch it again with your new config file.

We could have kept the previous DB and users, however in this lab we will start with a new empty database directory, meaning empty database.

Let's recreate the user m103-admin with the same requirements as earlier, as we will need this user for the validation scripts and later tasks.

Role: root on admin database
Username: m103-admin
Password: m103-pass
When you're finished, run the following validation script in your vagrant and outside the mongo shell and enter the validation key you receive below. If you receive an error, it should give you some idea of what went wrong.

vagrant@m103:~$ validate_lab_change_dbpath


ANSWER:
sudo mkdir /var/mongodb/db
sudo chown -R vagrant:vagrant /var/mongodb/db/
rm -rf mongod-27000.sock
mongo admin --host localhost:27000 --eval 'db.createUser({ user: "m103-admin", pwd: "m103-pass", roles: [{role: "root", db: "admin"}]})'

# mongod.conf
# Where and how to store data.
storage:
  dbPath: /var/mongodb/db/

# where to write logging data.
systemLog:
  destination: file
#  logAppend: true
  path: /var/log/mongodb/mongod.log

# network interfaces
net:
  port: 27000
  bindIp: "127.0.0.1,192.168.103.100"

# how the process runs
processManagement:
#  timeZoneInfo: /usr/share/zoneinfo
  fork: true

security:
  authorization: enabled
