"""
You have been given a string of lowercase letters.

Write a function called first_non_repeating_char(string) 
that finds the first non-repeating character in the given 
string using a hash table (dictionary).
 If there is no non-repeating character in the string, 
 the function should return None.

For example, if the input string is "leetcode", 
the function should return "l" because "l" is the first character
 that appears only once in the string. 
 Similarly, if the input string is "hello", 
 the function should return "h" because "h" is 
 the first non-repeating character in the string.

"""

def first_non_repeating_char(string):
    my_dict={}

    for char in string:
        my_dict[char] = my_dict.get(char, 0) + 1

    for key, val in my_dict.items(): # they are ordered!
        if val == 1:
            return key



print(first_non_repeating_char("leetcode"))