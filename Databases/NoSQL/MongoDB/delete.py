"""

Delete Document
To delete one document, we use the delete_one() method.

The first parameter of the delete_one() method is a query object defining which document to delete.

Note: If the query finds more than one document, only the first occurrence is deleted.

"""

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:2717/")
mydb = myclient["test"]
mycol = mydb["users"]

# Delete the document with the address "Mountain 21"

myquery = {"address": "Mountain 21"}

mycol.delete_one(myquery)

"""

Delete Many Documents
To delete more than one document, use the delete_many() method.

The first parameter of the delete_many() method is a query object defining which documents to delete.

"""

myquery = {"address": {"$regex": "^S"}}

x = mycol.delete_many(myquery)

print(x.deleted_count, " documents deleted.")


"""

Delete All Documents in a Collection
To delete all documents in a collection, pass an empty query object to the delete_many() method:

"""

x = mycol.delete_many({})

print(x.deleted_count, " documents deleted.")
