"""
Max heap, elements with a higher value have a higher priority
Important characteristic, heap invariant or heap property

    10_________________________ 1 _______Level 1
   /  \                        / \
   8   4 ____________________ 2  4 _____Level 2
  / \                         / \
 5   1 _____________________ 5   8 ______Level 3

 Max heap                       Min heap

Max heap, parent nodes must always contain a value that is greater than or equal to the value of the child
Root node always contains the highest value

Heap must be a complete binary tree. Every level must be filled

Applications: Calculate the miniume and maximum element of a collection, heap sort, constructing priority queue, and graph algorithms
(Prim and Dijkstra)
"""
class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        pass

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        pass

    def _sift_down(self, index):
        pass
