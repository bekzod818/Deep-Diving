"""

Limit the Result
To limit the result in MongoDB, we use the limit() method.

The limit() method takes one parameter, a number defining how many documents to return.

"""

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:2717/")
mydb = myclient["test"]
mycol = mydb["users"]

# Limit the result to only return 5 documents

myresult = mycol.find().limit(5)

# print the result:
for x in myresult:
    print(x)
