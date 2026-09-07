 

# def two_sum(arr, target):
#     output_arr = []
#     for i in range(len(arr)):
#         num1_index = 0
#         while num1_index < len(arr) - 1:
#             num2_value = target - arr[num1_index]

#             if num2_value in arr[num1_index+ 1:]:
#                 num2_index = arr.index(num2_value, num1_index + 1)
#                 output_arr.extend([num1_index, num2_index])
#                 return output_arr
#             else: 
#                 num1_index += 1
#         return output_arr


def two_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]

    return []


# print(two_sum(my_list, sum))
print(two_sum([5, 1, 7, 2, 5, 3], 10))  
print(two_sum([4, 2, 11, 7, 6, 3], 9))  
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))  
print(two_sum([1, 3, 5, 7, 9], 10))  
print ( two_sum([1, 2, 3, 4, 5], 10) )
print ( two_sum([1, 2, 3, 4, 5], 7) )
print ( two_sum([1, 2, 3, 4, 5], 3) )
print ( two_sum([], 0) )    


    