######### Filter the Result  #########

import pymongo

client = pymongo.MongoClient("mongodb://localhost:2717/")
db = client["test"]
collection = db["users"]

# When finding documents in a collection, you can filter the result by using a query object.

# The first argument of the find() method is a query object, and is used to limit the search.

myquery = {"address": "Park Lane 38"}

mydoc = collection.find(myquery)  # returns all documents by filtering myquery

for x in mydoc:
    print(x)

# Advanced Query

# To make advanced queries you can use modifiers as values in the query object.

# E.g. to find the documents where the "address" field starts with the letter "S" or higher (alphabetically), use the greater than modifier: {"$gt": "S"}:

myquery = {"address": {"$gt": "S"}}

mydoc = collection.find(myquery)

for x in mydoc:
    print(x)

# Find documents where the address starts with the letter "S" or higher:

####### Filter With Regular Expressions  #######

# Regular expressions can only be used to query strings.

# To find only the documents where the "address" field starts with the letter "S", use the regular expression {"$regex": "^S"}:

myquery = {"address": {"$regex": "^S"}}

mydoc = collection.find(myquery, {"_id": 0})

for x in mydoc:
    print(x)

# Find documents where the address starts with the letter "S":
