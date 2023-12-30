import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:2717/")

mydb = myclient["test"]

# database created!

print(myclient.list_database_names())
