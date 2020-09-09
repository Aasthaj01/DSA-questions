# Heap data structure is Tree-based data structure in which the tree is a complete binary tree. Generally, Heaps can be of two types:
#Max-Heap: In a Max-Heap the key present at the root node must be greatest among the keys present at all of it’s children. The same property must be recursively true for all sub-trees in that Binary Tree.
#Min-Heap: In a Min-Heap the key present at the root node must be minimum among the keys present at all of it’s children. The same property must be recursively true for all sub-trees in that Binary Tree.

# implementation of heap using heapq library
from heapq import heappush, heappop, heapify
heap = [] 
heapify(heap) 
arr = list(map(int, input().split()))
n = len(arr)
for i in range(n):
    heappush(heap, arr[i]) 
   
print("Head value of heap : "+str(heap[0])) 
print("The heap elements : ") 
for i in heap: 
    print(i, end = ' ') 
print() 
element = heappop(heap) 
print("The heap elements after removing head: ") 
for i in heap: 
    print(i, end = ' ') 
