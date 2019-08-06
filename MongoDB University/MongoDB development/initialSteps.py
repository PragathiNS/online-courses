# 1. CONNECT:
# Connect to MongoDB instance running on localhost
client = pymongo.MongoClient()

# Access the 'restaurant' collection in the 'test' database
collection = client.test.restaurant

# 2. INSERT A DOCUMENT:
new_documents = [
  {
	"name": "Sun Bakery Trattoria",
    "stars": 4,
    "categories": ["Pizza","Pasta","Italian","Coffee","Sandwiches"]
  }, {
    "name": "Blue Bagels Grill",
    "stars": 3,
    "categories": ["Bagels","Cookies","Sandwiches"]
  }, {
    "name": "Hot Bakery Cafe",
    "stars": 4,
    "categories": ["Bakery","Cafe","Coffee","Dessert"]
  }, {
    "name": "XYZ Coffee Bar",
    "stars": 5,
    "categories": ["Coffee","Cafe","Bakery","Chocolates"]
  }, {
    "name": "456 Cookies Shop",
    "stars": 4,
    "categories": ["Bakery","Cookies","Cake","Coffee"]
  }
]

collection.insert_many(new_documents)

# 3. QUERY 

# Get all the documents in the restaurant collection and store them as an array
for restaurant in collection.find():
	pprint.pprint(restaurant)
  
# 4. CREATE INDEX

# we are building an index on the name field with sort order ascending.
collection.create_index([('name', pymongo.ASCENDING)])

# 5. AGGREGATE

# we pull all the documents in the restaurants collection that have a category of Bakery using the $match operator and then group them by their star rating using the $group operator. Using the accumulator operator, $sum, we can see how many bakeries in our collection have each star rating.
pipeline = [
  {"$match": {"categories": "Bakery"}},
  {"$group": {"_id": "$stars", "count": {"$sum": 1}}}
]

pprint.pprint(list(collection.aggregate(pipeline)))