class MaxHeap:
    def __init__(self):
        self.my_heap = []

    def _right_child(self, index):
        return 2 * index + 2
    
    def _left_child(self, index):
        return 2 * index + 1
    
    def _parent(self, index):
        return (index-1) // 2
    
    def _swap(self, index1, index2):
        self.my_heap[index1], self.my_heap[index2] = self.my_heap[index2], self.my_heap[index1]

    def insert(self, value):
        # Step 1: insert it at the end - Complete Heap
        self.my_heap.insert(value)
        current_idx = len(self.my_heap) -1
        # Step 2 - MOve it up
        while current_idx > 0 and self.my_heap[current_idx] > self.my_heap[self._parent(current_idx)]:
            self._swap(current_idx, self._parent(current_idx)) 
            current_idx = self._parent(current_idx)


