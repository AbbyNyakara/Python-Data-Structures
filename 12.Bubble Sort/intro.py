def bubble_sort(my_list):
    for i in range(len(my_list)-1, 0, -1): # i = 5 in round 1 if the list has 6 items
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list


print(bubble_sort([2,5,7,4,3]))

    