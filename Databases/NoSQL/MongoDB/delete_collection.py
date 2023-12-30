import pymongo

# You can delete a table, or collection as it is called in MongoDB, by using the drop() method.

client = pymongo.MongoClient("mongodb://localhost:2717/")

db = client["test"]

collection = db["users"]

collection.drop()

# The drop() method returns true if the collection was dropped successfully, and false if the collection does not exist.

print(db.list_collection_names())  # return list without 'users' collection name
