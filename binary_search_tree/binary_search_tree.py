import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check the value against the node's value
        # if value is less than value, go left
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        # if value is greater, go right
        else:
            # if the node.right is true, recurse
            if self.right:
                self.right.insert(value)
            else:
                # if the node.right is empty, store our node
                self.right = BinarySearchTree(value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
        else:
            if self.right:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # max_value = self.value
        # while self:
        #     if self.value > max_value:
        #         max_value = self.value
        #     self = self.right # GOTCHA, storing variables can get you stuck in infinite loops
        # return max_value

        # Assumes we have balanced tree
        max_value = self.value
        while self.right:
            max_value = self.right.value
            self = self.right
        return max_value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
