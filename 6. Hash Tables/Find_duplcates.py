def find_duplicates(nums):
    my_hash = {}
    duplicated_nos = []
    
    for num in nums:
        if num not in my_hash:
            my_hash[num] = True
            
        else:
            duplicated_nos.append(num)
            
    return duplicated_nos
    



def find_duplicates1(nums):
    num_counts = {}
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1
 
    duplicates = []
    for num, count in num_counts.items():
        if count > 1:
            duplicates.append(num)
 
    return duplicates

