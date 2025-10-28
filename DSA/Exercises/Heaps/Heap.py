
# Heapsort??
# 

# A heap is a tree-based data structure that satisfies the heap property: 
#   Max heap: for any given node, their parent's value must be >= that of the node.
#   Min heap: for any given node, their parent's value must be <= that of the node.

# Operations
#   Basic:
#       Find / peek: Return max/min val of heap
#       Extract / pop: Remove and return max/min val of heap
#       Delete: Remove max/min val of heap
#       Insert / push: Add node to heap
#       Replace: Pop root and push new node *How's it implemented?
#   Creation:
#       Create: Create empty heap
#       Heapify: Create heap out of an array
#       Merge: Join two heaps, preserving originals
#       Meld: Join two heaps, destroying originals
#   Inspection:
#       Size: Return node count
#       IsEmpty: Returns whether heap is empty
#   Internal:
#       Update: Update value of existing node
#       Delete: Delete node and re-balance
#       SiftUp: Move node up until restoring heap condition after insertion.
#       SiftDown: Move node down until restoring heap condition after deletion or replacement

# Implementation:
#   Heap is usually implemented as an array
#   The first index is the root. 
#   Then, the rest are filled as follows:
#       A parent at index k, has children at indexes
#       2k + 1 and 2k + 2.
#       Inversely, for a given children at i,
#       the parent is at k = (i-1) // 2      
#   Thus, each 'level', can be found as
#   level = int(log_2 (count))

from typing import List
from math import inf
# Improvements:
# index: should save a dictionary with index of element instead of a set and doing linear search
# Merge: needs fixing
# Delete: is not exact heap behavior?
# Update - maybe something fishy
# 
class BinaryHeap:
    # Initialize binary heap
    def __init__(self, ls: List[int]):
        self.heap: List[int] = [] 
        self.idxs = {}
        self.heapify(ls)
        return

    # Return size of heap
    def size(self) -> int:
        return len(self.heap)
    
    # Return whether heap is empty
    def isEmpty(self) -> bool:
        return self.size() == 0
    
    # Return whether heap contains element
    def contains(self, val: int) -> bool:
        return val in self.idxs
    
    # Return index of element
    def index(self, val: int) -> int:
        if not self.contains(val):
            return -1
        
        return self.idxs[val]
        
    # Make heap out of a list
    # TODO: More efficient way with bottom up
    def heapify(self, ls: List[int]):
        if not ls: return

        # Add element by element to the heap
        for val in ls:
            self.insert(val)
        return

    # Return max/min val of heap
    def peek(self) -> int:
        if self.isEmpty(): 
            return
        
        return self.heap[0]
    
    # Remove and return max/min val of heap
    def pop(self) -> int:
        if self.isEmpty():
            return
        
        mx = self.peek()        
        self.delete(mx)
        return mx

    # Remove node from heap
    def delete(self, val: int):
        if not self.contains(val): 
            return
        
        idx = self.index(val)
        last = self.heap.pop()
        del self.idxs[val]
        if idx >= self.size():
            return

        # Replace with last value
        self.heap[idx] = last 
        self.idxs[last] = idx

        # Switch into correct pos. Can be up or down
        self._siftDown(idx)
        self._siftUp(idx)
        return

    # Add node to heap
    def insert(self, val: int):
        if self.contains(val): 
            return

        self.heap.append(val)
        # Start at bottom on the newly added element
        idx = self.size() - 1
        self.idxs[val] = idx 
        self._siftUp(idx)
        return

    # Update value of existing node
    def update(self, val: int, newVal: int):
        if not self.contains(val) or self.contains(newVal): 
            return

        # Replace old with new one
        idx = self.index(val)
        self.heap[idx] = newVal
        del self.idxs[val]
        self.idxs[newVal] = idx

        # Switch into correct pos. Can be up or down
        self._siftDown(idx)
        self._siftUp(idx)
        return
    
    # Combine heap with given one
    # TODO: Check if heap2 a heap? Diff process if it isn't? 
    def merge(self, heap2: List[int]) -> List[int]:
        for node in heap2:
            if not node: continue
            self.insert(node)
        
        return self.heap
    
    # Move node up until restoring heap condition 
    def _siftUp(self, idx: int):
        c = idx

        # Switch children (c) with parent (p) as needed to mantain heap condition
        while c > 0:
            p = (c - 1) // 2
            if not self._switch(p, c): break
            c = p
        return

    # Move node down until restoring heap condition
    def _siftDown(self, idx: int):
        p = idx
        n = self.size()

        # Switch parent (p) with children (c) as needed to mantain heap condition
        while (2*p + 1 < n):
            # Switch with largest of the children
            c1, c2 = 2*p + 1, 2*p + 2
            c = c1 if (c2 >= n) or (self.heap[c1] >= self.heap[c2]) else c2

            if not self._switch(p, c): break
            p = c

        return
    
    def _switch(self, p: int, c: int):
        parent, child = self.heap[p], self.heap[c]
        if parent > child: return False
        self.heap[p], self.heap[c] = child, parent
        self.idxs[parent], self.idxs[child] = self.idxs[child], self.idxs[parent]
        return True

# Generalize for more heaps
class HeapTester():
    def __init__(self, heap):
        self.obj = heap
        self.heap = self.obj.heap
        self.results = []
        self.snapshots = []

    def output(self):
        print(self.heap)

    # TODO: Maybe pretty output?
    def prettyOutput(self):
        self.output()
    
    # Call a method on the heap
    def call(self, action: str, *args):
        method = getattr(self.obj, action)   # look up method by name
        return method(*args)
    
    # Alternative: by reference
    # def call(self, action, *args):
    #     return action(*args)

    # Call and store output
    def check(self, action: str, *args):
        res = self.call(action, *args)
        self.results.append(res)
        # self.snapshots.append(self.heap)
        args_str = ", ".join(map(str, args))

        print(f"{action} ({args_str}): {res}. Heap = [{', '.join(map(str, self.heap))}]")
        return res

    # Run a batch of actions [(name, args, kwargs), ...]
    def checkAll(self, actions: list[tuple]):
        for action, args in actions:
            self.check(action, *args)
        return self.results
    

if __name__ == "__main__":
    ls = [1,2,6,10,3,4,5]
    h = BinaryHeap(ls)
    tester = HeapTester(h)
    actions = [
        ("insert", (3,)),
        ("pop", ()),
        ("insert", (4,)),
        ("pop", ()),
        ("update", (3, 100)),
        ("delete", (1,))
    ]
    results = tester.checkAll(actions)
    