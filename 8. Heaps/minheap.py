class MinHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return index * 2 + 1

    def _right_child(self, index):
        return index * 2 + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]


    def insert(self, value):
        self.heap.append(value)

        current = len(self.heap) - 1 # this point to the last index

        while current > 0 and self.heap[current] < self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)


minheap = MinHeap()
minheap.insert(12)
minheap.insert(17)
minheap.insert(25)
minheap.insert(34)
minheap.insert(60)
minheap.insert(40)
minheap.insert(70)

print(minheap.heap)

print("===============")
minheap.insert(22)

print(minheap.heap)

