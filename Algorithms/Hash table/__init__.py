class HashTable:
    def __init__(self):
        self.table = {}

    def hash(self, key: str):
        hash_value = 0
        for i in key:
            hash_value += ord(i)
        return hash_value

    def index(self, key):
        return self.hash(key=key)

    def set(self, key, value):
        index = self.index(key=key)
        self.table[index] = value

    def get(self, key):
        index = self.index(key=key)
        return self.table[index]


my_hash_table = HashTable()
my_hash_table.set("name", "Bekzod")
my_hash_table.set("age", 23)
my_hash_table.set("city", "Showot")

print(my_hash_table.get("name"))
print(my_hash_table.get("age"))
print(my_hash_table.get("city"))
