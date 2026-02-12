'''
Docstring for 10. Practice Questions.4.Twosum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

'''



class Solution:
    def twoSum(self, nums, target: int):
        for idx, first_number in enumerate(nums):
            needed_number = target - first_number

            try:
                second_number = nums.index(needed_number, idx+1, len(nums)) # Only search forward: exclude the first number

                output = [idx, second_number]
                break
            except ValueError:
                continue

        return output
