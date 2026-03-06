class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_hash(self):
        for key, value in enumerate(self.data_map):
            print(key, ":", value)

    def set_value(self, key, value):
        index = self.__hash(key)

        if self.data_map[index] == None:
            self.data_map[index] = []  # Create an empty list here
            # Append to the data_map
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)

        if self.data_map[index] is None:
            return None

        for item in self.data_map[index]:
            if item[0] == key:
                return item[1]
        return None

    def keys(self):
        """
        Returns all the keys 
        """
        all_keys = []
        for index in range(len(self.data_map)):
            if self.data_map[index] is not None:
                for item in self.data_map[index]:
                    all_keys.append(item[0])

        return all_keys
    
        # all_keys = []
        
        # for index, bucket in enumerate(self.data_map):
        #     if bucket is not None:
        #         for item in bucket:      # item is [key, value]
        #             all_keys.append(item[0])
        
        # return all_keys

        
