"""
This is when the heap starts from index 0 and not 1
"""


class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _sink_down(self, index):
        pass

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def remove(self):
        # Removes the node from the Heap
        # TODO 1 - When its empty
        if self.heap == 0:
            return None

        # TODO 2 - When there is only one value in the node.
        if self.heap == 1:
            return self.heap.pop()

        # TODO 3 - When there is 2 or more

        max_value = self.heap.pop(0)

        self.heap[0] = self.heap.pop()

        self._sink_down(0)

        return max_value





            
my_heap = MaxHeap()
my_heap.insert(99)
my_heap.insert(72)
my_heap.insert(61)
my_heap.insert(58)
my_heap.insert(100)
print(my_heap.heap)