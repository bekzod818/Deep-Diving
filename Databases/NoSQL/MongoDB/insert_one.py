# A document in MongoDB is the same as a record in SQL databases.

import pymongo

client = pymongo.MongoClient("mongodb://localhost:2717/")
db = client["test"]
collection = db["users"]

# To insert a record, or document as it is called in MongoDB, into a collection, we use the insert_one() method.

data = {"name": "John Doe", "address": "Highway, 37"}

# The first parameter of the insert_one() method is a dictionary containing the name(s) and value(s) of each field in the document you want to insert.

record = collection.insert_one(data)

# The insert_one() method returns a InsertOneResult object, which has a property, inserted_id, that holds the id of the inserted document.

print(record.inserted_id)

# If you do not specify an _id field, then MongoDB will add one for you and assign a unique id for each document.

# In the example above no _id field was specified, so MongoDB assigned a unique _id for the record (document).
