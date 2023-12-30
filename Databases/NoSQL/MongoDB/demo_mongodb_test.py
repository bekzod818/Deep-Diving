import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:2717/")

# You can check if a database exist by listing all databases in you system:

print(myclient.list_database_names())

# Check if "test" exists:

dblist = myclient.list_database_names()
if "test" in dblist:
    print("The database exists.")
