def solution(A):
    # For faster lookup convert to set:
    new_set = set(A)
    for number in range(1, len(A)+2):
        if number not in new_set:
            return number


list1 = [-3, -5, -6]
list2 = [-4, 1, 5]
list3 = [0, 1, 3, 5, 6]
list4 = [1, 2, 3, 4, 5]

print(solution(list1))
