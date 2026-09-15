"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

"""

# Change the list to a str
# Then string to a integer, 
# Add 1 and then reverse the entire process; 
# Typecasting 

def plusOne(digits: list[int]) -> list[int]:
    # Step 1 - Change the didgits into a string  - "123"
    my_string = "".join(map(str, digits))
    

    # Step 2 - change that into numbers type and do the operation
    my_numbers = int(my_string) + 1 # e.g 124
    

    # Step 3 - change that to a string 
    new_string = str(my_numbers)
    

    result = list(map(int, list(new_string)))
    print(result)

        # # Then back to a list of numbers
        # return map(int, list(new_string))
    
plusOne([9, 4])

## What is the more efficient way of soing it? 
        