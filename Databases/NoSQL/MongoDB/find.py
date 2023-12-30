# In MongoDB we use the find() and find_one() methods to find data in a collection.

# Just like the SELECT statement is used to find data in a table in a MySQL database.

import pymongo

client = pymongo.MongoClient("mongodb://localhost:2717/")
db = client["test"]
collection = db["users"]

# To select data from a collection in MongoDB, we can use the find_one() method.

record = collection.find_one()

# The find_one() method returns the first occurrence in the selection.

print(record)


# Find All. To select data from a table in MongoDB, we can also use the find() method.

# The find() method returns all occurrences in the selection.

# The first parameter of the find() method is a query object. In this example we use an empty query object, which selects all documents in the collection.

# No parameters in the find() method gives you the same result as SELECT * in MySQL.

for record in collection.find():
    print(record)

# Return Only Some Fields

# The second parameter of the find() method is an object describing which fields to include in the result.

# This parameter is optional, and if omitted, all fields will be included in the result.

for x in collection.find(
    {}, {"_id": 0, "name": 1, "address": 1}
):  # 0 - False, 1 - True
    print(x)

# You are not allowed to specify both 0 and 1 values in the same object (except if one of the fields is the _id field). If you specify a field with the value 0, all other fields get the value 1, and vice versa:

for x in collection.find({}, {"address": 0}):
    print(x)

# You get an error if you specify both 0 and 1 values in the same object (except if one of the fields is the _id field):

for x in collection.find({}, {"name": 0, "address": 1}):
    print(x)
