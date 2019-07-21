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
for restaurant in collection.find():
	pprint.pprint(restaurant)
  
