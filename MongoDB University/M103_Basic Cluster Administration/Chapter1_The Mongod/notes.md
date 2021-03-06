MongoDB Architecture

DataStructures:
1. Databases and Collections
	db.createCollection()
		Creates a collection on the chosen Database
	db.createUser()
	db.dropUser()
	db.runCommand()
		Effects the configuration or behavior of the Database

	Data is stores in Collections
	Each Database can contain multiple Collections

	use <Database name>
	show dbs

2. Indexes
	Stores a small portion of the collection's data set in the form that's easy to traverse
	supports efficient queries
	If not used, then MongoDB does a linear search through the entire collection (Collection Scan)
	However, indexes takes up space in memory, so we shouldn't create indexes unless it supports our queries
	Each index that we create, increases the write overhead on the collection


MongoDB Documents:
	Hierarchical structure
	Database > Collections > Documents
	JSON and XML format
	It's like a row in SQL database
	MongoDB does have Schema but Documents are Schemaless
	MongoDB documents are restricted to 16MB in size
	Attempting to insert or update a document beyond that size results in an error
	Storage layer stores data in BSON format and the drivers in between Storage and Application Layer, translates the BSON to JSON
	MongoDB is extended to support all BSON dataTypes format
	MongoDB presents documents as JSON, but stores them as BSON

	JSON DataTypes
	- Object
	- String
	- Number
	- Array
	- Boolean
	- Null

	BSON DataTypes
	- String		- Symbol
	- Double            	- 32-bit integer
	- Binary Dare       	- TimeStamp
	- Undefined         	- 64-bit integer
	- ObjectId          	- Decimal128
	- Regular Expression	- MinKey
	- DBPointer         	- MaxKey
	- JavaScript		- Object
	- Array			- Boolean
	- Null

MongoDB Configuration File
		It's a way to organize the options you need to run the MongoD or Mongos process into an easy to parse XML into YAML file
		Configure MongoD/S storage options

		MongoD Configuration File and Command Line option
			storage.dbPath 								--dbpath
			systemLog.path and systemLog.destination	--logpath
			net.bind_ip									--bind_ip (To include a n/w adapter on the host that provides access to the network otherwise MongoD can accept connections only on that host)
			replication.replSetName						--replSet
			security.keyFile							--keyFile (starts up the MongoD in replication mode with basic intercluster and auth security and user authentication enabled.)
			net.ssl.sslPEMKey							--sslPEMKey
			net.ssl.sslCAKey							--sslCAKey
			net.sslMode									--sslMode (Related to TLS SSL transport encryption)
			processManagement.fork						--fork (Tells MongoD to run as daemon instead of being tied to a terminal window)

		Command Line:
		mongod --dbpath /data/db --logpath /data/log/mongod.log --fork --replSet "M103" --keyFile /data/keyfile --bind_ip "127.0.0.1,192.168.0.100" --sslMode requireSSL --sslCAFile "/etc/ssl/SSLCA.pem" --sslPEMKeyFile "/etc/ssl/ssl.pem"

		Yet Another Markup Language
			key value pairs
			storage:
				dbPath: "/data/db"
			systemLog:
				path: "/data/log/mongod.log"
				destination: "file"
			replication:
				replSetName: "M103"
			net:
				bindIp: "127.0.0.1, 192.168.0.10"
				ssl:
					mode: "requireSSL"
					PEMKeyFile: "/etc/ssl/ssl.pem"
					CAFile: "/etc/ssl/SSLCA.pem"
			security:
				keyFile: "/data/keyfile"
			processManagement:
				fork: true

		how to use the configuration:
		> mongod --config "etc/mongod.conf"
		OR
		> mongod -f "/etc/mongod.conf"

File structure


Basic Commands:
	Basic Helper groups
	1. db.<method>() --> wrap Commands that interacts with the DB
		 One additional extension -> db.<collection>.<method>() --> collection level operators
	2. rs.<method>() --> wrap commands that control replica set deployment and management
	3. sh.<method>() --> wrap commands to control sharded cluster deployment and management

User management
db.createUser()
db.dropUser()

Collection management
db.renameCollection()
db.collection.createIndex()
db.collection.drop()

Database management
db.dropDatabase() --> deleted all collections, indexes, documents, users on the DB
db.createCollection()

Database status
db.serverStatus()

Database command Vs Shell Helper
db.runCommand( { <COMMAND> } )
db.commandHelp( "<command>" ) --> introspect a shell Helper
db.runCommand(											
	{
		"createIndexes": "<collection>",
		"indexes" : [
		{
			key: {"product": 1}
		},
		"name": "name_index"
		]
	}
)

db.<collection>.createIndex(
	{"product": 1},
	{"name": "name_index"}
)

Logging Basics:
2 logging facilities for tracking activities on the Database
Process log
-> displays activities on the mondgoDB instances
-> collects activities to one of the following Components [ use db.getLogComponents() in the mongo shell]


Log Messages Severity levels:
F	Fatal
E	error
W	Warning
I Informational (verbosity level 0)
D Debug (Verbosity level 1-5)

Get the logging components:
mongo admin --host 192.168.103.100:27000 -u m103-admin -p m103-pass --eval 'db.getLogComponents()'

Change the logging level:
mongo admin --host 192.168.103.100:27000 -u m103-admin -p m103-pass --eval 'db.setLogLevel(0, "index")'

Tail the log file:
tail -f /data/db/mongod.log

Update a document:
mongo admin --host 192.168.103.100:27000 -u m103-admin -p m103-pass --eval 'db.products.update( { "sku" : 6902667 }, { $set : { "salePrice" : 39.99} } )'

Look for instructions in the log file with grep:
grep -R 'update' /data/db/mongod.log
