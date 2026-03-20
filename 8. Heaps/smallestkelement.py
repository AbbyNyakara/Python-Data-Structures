"""
You are given a list of numbers called nums and a number k.

Your task is to write a function find_kth_smallest(nums, k) to find the kth smallest number in the list.

The list can contain duplicate numbers and k is guaranteed to be within the range of the length of the list.

This function will take the following parameters:

nums: A list of integers.

k: An integer.



This function should return the kth smallest number in nums.



Example 1:

nums = [3, 2, 1, 5, 6, 4]
k = 2
print(find_kth_smallest(nums, k))
In the example above, the function should return 2. If we sort the list, it becomes [1, 2, 3, 4, 5, 6]. The 2nd smallest number is 2, so the function returns 2.



Example 2:

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(find_kth_smallest(nums, k))
In the example above, the function should return 3. If we sort the list, it becomes [1, 2, 2, 3, 3, 4, 5, 5, 6]. The 4th smallest number is 3, so the function returns 3.

Note: For the purpose of this problem, we assume that duplicate numbers are counted as separate numbers. For example, in the second example above, the two 2s are counted as the 2nd and 3rd smallest numbers, and the two 3s are counted as the 4th and 5th smallest numbers.

Please write your solution in Python and use a max heap data structure to solve this problem. The MaxHeap class is provided for you.
"""


class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _parent(self, index):
        return (index - 1) // 2

    def insert(self, value):
        self.heap.append(value)

        current_idx = len(self.heap) - 1

        while self.heap[current_idx] > self.heap[self._parent(current_idx)] and current_idx > 0:
            self._swap(current_idx, self._parent(current_idx))
            current_idx = self._parent(current_idx)

    def _sink_down(self, index):
        max_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index

            if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index

            else:
                return

    def remove(self):
        if self.heap == 0:
            return None

        if self.heap == 1:
            return self.heap.pop(0)
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)

        return max_value


def find_kth_smallest(nums, k):
    my_heap = MaxHeap()  # Initialize empty heap

    for num in nums:
        if len(my_heap.heap) < k:
            my_heap.insert(num)

            max_value = my_heap.heap[0]

            if num < max_value:
                my_heap.remove()  # remove the number at the root
                my_heap.insert(num)
            else:
                continue

    return my_heap.heap[0]



def find_kth_smallest_inefficient(nums, k):
    return sorted(nums)[k-1]



# my_heap = MaxHeap()
# my_heap.insert(10)
# my_heap.insert(87)
# my_heap.insert(99)
# my_heap.insert(20)


# print(my_heap.heap)

# print("==========")

# my_heap.remove()

# print(my_heap.heap)

print(find_kth_smallest_inefficient([3,2,3,1,2,4,5,5,6], 7))
