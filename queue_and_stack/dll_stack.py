import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList, ListNode

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_from_tail()

    def len(self):
        return self.size


class DoubleStack:
    def __init__(self):
        self.leftStack = Stack()
        self.rightStack = Stack()

    def isEmpty(self):
        return True if self.leftStack.len() == 0 and self.rightStack.len() == 0 else False

    def peek(self):
        return self.leftStack[-1] if self.leftStack.len() == 0 else self.rightStack[0]