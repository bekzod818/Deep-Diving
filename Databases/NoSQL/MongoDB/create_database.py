import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:2717/")

# Remember: In MongoDB, a database is not created until it gets content, so if this is your first time creating a database, you should complete the next two chapters (create collection and create document) before you check if the database exists!

mydb = myclient["test"]  # database created!
