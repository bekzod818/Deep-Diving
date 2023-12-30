"""

Sort the Result
Use the sort() method to sort the result in ascending or descending order.

The sort() method takes one parameter for "fieldname" and one parameter for "direction" (ascending is the default direction).

"""

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:2717/")
mydb = myclient["test"]
mycol = mydb["users"]

mydoc = mycol.find().sort("name")  # ascending by default 'name' field (A-Za-z)

for x in mydoc:
    print(x)


"""

Sort Descending
Use the value -1 as the second parameter to sort descending.

sort("name", 1) #ascending
sort("name", -1) #descending

"""

# Sort the result reverse alphabetically by name:

mydoc = mycol.find().sort("name", -1)

for x in mydoc:
    print(x)
