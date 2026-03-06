# Time complexity of O(N^2)
def items_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
            
def common_items(list1, list2):
    my_dictionary = {}

    for item in list1:
        my_dictionary[item] = True

    for item in list2:
        if item in my_dictionary:
            return True
        

print(common_items([1, 5, 6], [4, 3, 5]))