# head = [5, 6, 7, 8]
# k = 3

# def removeKthNodeFromEnd(head, k):
#     my_dict = {}
#     starting_index = 0

#     for num in head[::-1]:
#         my_dict[num] = starting_index
#         starting_index += 1

#     # Now we have a populated dictionary
#     # REmove the k=3 
#     # 
     
#     for key, value in my_dict.items():
#         if value == k:
#             del my_dict[k] 

#     return my_dict.keys() # the 3 is the value here and not the key 

# print(removeKthNodeFromEnd(head, k))



head = [1, 5, 1]
k = 5

def removeKthNodeFromEnd(head, k):
    my_dict = {}
    starting_index = 0

    # Build dictionary with 0-based index from the end
    for num in head[::-1]:
        my_dict[starting_index] = num
        starting_index += 1

    # Check if k is a valid index
    if k not in my_dict:
        return head

    # Get the value we want to delete
    key_to_delete = my_dict[k]

    # Build the result in the original order
    result = [i for i in head if i != key_to_delete]

    return result


print(removeKthNodeFromEnd(head, k))


