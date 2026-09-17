"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""

def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    if list1 is None and list2 is None:
        return []
    # Compare list1 and list2 (at the head), start with the node with the least
    # If there are equal, start with list1 (or list2) Doesnt really matter
    

    # Move the pointer along, comparing the numbers, and changing the next pointer 



    # do that as long as list1 and list2 are not None



    

