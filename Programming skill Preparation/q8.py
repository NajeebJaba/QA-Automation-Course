# Question 8

##################  Hash Tables: ##################

#a. Implement a hash table and write functions to insert, delete, and search for elements.

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)

        # Collision handling with chaining (using lists)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (existing_key, _) in enumerate(self.table[index]):
                if existing_key == key:
                    # Update value if key already exists
                    self.table[index][i] = (key, value)
                    break
            else:
                # Key doesn't exist, add a new entry
                self.table[index].append((key, value))

    def delete(self, key):
        index = self._hash_function(key)

        if self.table[index] is not None:
            for i, (existing_key, _) in enumerate(self.table[index]):
                if existing_key == key:
                    del self.table[index][i]
                    break

    def search(self, key):
        index = self._hash_function(key)

        if self.table[index] is not None:
            for existing_key, value in self.table[index]:
                if existing_key == key:
                    return value

        return None  # Key not found

# Test the hash table to verify if it's running well
# hash_table = HashTable(size=10)
#
# # Insert elements
# hash_table.insert("one", 1)
# hash_table.insert("two", 2)
# hash_table.insert("three", 3)
#
# # Search elements
# print("Search 'two':", hash_table.search("two"))  # Output: 2
#
# # Delete an element
# hash_table.delete("two")
#
# # Search after deletion
# print("Search 'two':", hash_table.search("two"))  # Output: None


