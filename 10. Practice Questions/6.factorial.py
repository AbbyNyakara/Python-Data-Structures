"""
Find the factorial of a number
# Use recursion
Determine the base case

"""

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)

print(factorial(4))
