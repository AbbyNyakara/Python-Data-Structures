def print_numbers(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


# print_numbers(10)

# This will print 100 numbers.
"""
See those two for loops? For each item in the list, the inner loop
runs through the entire list again. If the list has 10 items, 
that’s 10 × 10 = 100 operations. If it has 1,000 items, that’s 1,000 × 1,000 = 
1,000,000 operations! That’s O(n²) – the number of operations grows quadratically as 
the list size increases. 
"""


def find_duplicates(list):
    for i in list:
        list.remove(i)  # remove the number so it does not compare to itself:
        for j in list:
            if i == j:
                print(i)


find_duplicates([1, 3, 4, 5, 6, 7, 2, 1])
