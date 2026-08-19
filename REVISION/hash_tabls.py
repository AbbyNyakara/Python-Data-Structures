class HashTable:
    def __init__(self, size=7): # This creates the empty list / hash table
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0

        for letter in key: # Assuning the key is a string: 
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
            # my_hash = (my_hash* 23 + ord(letter)) % len(self.data_map) This is a different approach i would use: 
        return my_hash

    

    