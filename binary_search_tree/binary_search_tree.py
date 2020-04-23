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

        # iterative solution, with stack, depth-first approach, (LIFO)
        # stack = Stack()
        # stack.append(self)
        # while len(stack) > 0:
        #     curr = stack.pop()
        #     if curr.right:
        #         stack.push(curr.right)
        #     if curr.left:
        #         stack.push(curr.left)
        #     cb(curr.value)

        # breadth-first approach, levels (FIFO)
        # queue = Queue()
        # queue.enqueue(self)
        # while len(queue):
        #     curr = queue.dequeue()
        #     print(curr)

        #     if curr.left:
        #         queue.enqueue(curr.left)
        #     if curr.right:
        #         queue.enqueue(curr.right)
        #     cb(curr.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal (LIFO)
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self)

        print(self.value)

        if self.right:
            self.right.in_order_print(self)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal (FIFO)
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(self)
        while queue.len():
            current_node = queue.dequeue()
            print(current_node.value)

            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal (LIFO)
    def dft_print(self, node):
        stack = Stack()
        stack.push(self)
        while stack.len():
            popped_element = stack.pop()
            print(popped_element.value)

            if popped_element.right:
                stack.push(popped_element.right)
            if popped_element.left:
                stack.push(popped_element.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass



bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)
bst.bft_print(bst)
print("-------")
bst.dft_print(bst)