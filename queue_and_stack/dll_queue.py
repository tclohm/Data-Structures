import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

# LIFO
class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.len() == 0:
            return "Please enqueue a node before trying dequeuing, the queue is empty"
        self.storage.remove_from_head()

    def len(self):
        return len(self.storage)
