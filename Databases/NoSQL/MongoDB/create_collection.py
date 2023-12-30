# A collection in MongoDB is the same as a table in SQL databases.

import pymongo

client = pymongo.MongoClient("mongodb://localhost:2717/")
db = client["test"]

# To create a collection in MongoDB, use database object and specify the name of the collection you want to create.
collection = db["users"]  # collection created!

# Important: In MongoDB, a collection is not created until it gets content!

# You can check if a collection exist in a database by listing all collections:

print(db.list_collection_names())

# Or you can check a specific collection by name:

collections_list = db.list_collection_names()

if "users" in collections_list:
    print("The collection exists!")
