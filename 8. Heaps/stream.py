"""
Write a function named stream_max that takes as its input a list of integers (nums). 
The function should return a list of the same length, where each element in the output
 list is the maximum number seen so far in the input list.

More specifically, for each index i in the input list, 
the element at the same index in the output list should be the maximum value among
 the elements at indices 0 through i in the input list.

Use the provided MaxHeap class to solve this problem. You should not need
 to modify the MaxHeap class to complete this task.

Function Signature: def stream_max(nums):
Examples:

If the input list is [1, 3, 2, 5, 4], the function should return [1, 3, 3, 5, 5].
Explanation:

At index 0, the maximum number seen so far is 1.
At index 1, the maximum number seen so far is 3.
At index 2, the maximum number seen so far is still 3.
At index 3, the maximum number seen so far is 5.
At index 4, the maximum number seen so far is still 5.

So, the output list is [1, 3, 3, 5, 5].

Similarly, if the input list is [7, 2, 4, 6, 1], the function should return [7, 7, 7, 7, 7].
Explanation:
At each index, the maximum number seen so far is 7.
So, the output list is [7, 7, 7, 7, 7].
"""


class MaxHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, index):
        return (index-1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        # Bubble it up to the right position:

        current_idx = len(self.heap) - 1

        while self.heap[current_idx] > self.heap[self._parent(current_idx)] and current_idx > 0:
            self._swap(current_idx, self._parent(current_idx))

            current_idx = self._parent(current_idx)


def max_stream(nums):
    my_heap = MaxHeap()
    max_list = []
    for number in nums:
        my_heap.insert(number)
        current_max = my_heap.heap[0]

        max_list.append(current_max)

    return max_list

print(max_stream([-1, -2, -3, -4, -5]))
