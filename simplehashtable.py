def hash_func(key):
    return len(key) - 1

class HashTable:
    def __init__(self):
        self.items = [None] * 10
    def insert(self, key, value):
        i = hash_func(key)
        if i >= self.capacity():
            to_increase = ((i // 10) * 10 + 10) - self.capacity()
            self.items.extend([None] * to_increase)
        self.items[i] = value
    def retrieve(self, key):
        return self.items[hash_func(key)]
    def capacity(self):
        return len(self.items)

hash_table = HashTable()
hash_table.insert('Amy', 20)
hash_table.insert('John', 35)
hash_table.insert('Christopher', 27)
print(hash_table.retrieve('John'))

