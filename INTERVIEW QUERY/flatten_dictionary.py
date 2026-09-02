class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def _hash(self, key):
        address = 0

        for char in key:
            address = (address * 23 + ord(char) ) % len(self.data_map)

        return address

    def set_item(self, key, value):
        my_list = []
        address = self._hash(key)

        if self.data_map[address] is None:
            self.data_map[address] = []

        self.data_map[address].append([key, value])

        return self.data_map

    def get_item(self, key):
        """
        Takes in the key and returns the value from the hash table
        - some sought of value look up 
        """

        address = self._hash(key) # returns the address location. It is deterministic 

        if self.data_map[address] is None: # alternatively you can start by defining whrn ut is not None
            return None
        else: 
            for addr_list in self.data_map[address]:
                if addr_list[0] == key:
                    return addr_list[1]
                else:
                    return None







word1 = "cat"
word2 = "act"

hash = HashTable()
# print(hash._hash(word1))
# print(hash.set_item("abby", 32))
print(hash.set_item("car", "honda"))
print(hash.set_item("allan", 30))
print(hash.set_item("chris", 34))
# print(hash.set_item("hezbon", 34))
# print(hash._hash(word2))

print("Test the get item hash")
print(hash.get_item("abby"))
