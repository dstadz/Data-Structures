import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value == None:
            self.value = value
            return
        elif self.value <= value:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        else:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif self.value < target :
            if self.right:
                return self.right.contains(target)
            else:
                return False
        else:
            if self.left:
                return self.left.contains(target)
            else:
                return False


    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

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

        if self.left:
            return self.in_order_print(self.left)
            print(self.value)
            if self.right:
                return self.in_order_print(self.right)
        else:
            print

        if not self.left and not self.right:
            print(self.value)
            return

        if self.left:
            return self.left.in_order_print(self)





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


a = [4,3,9,2,0,1,5,8,7]
b = [8,5,7,6,3,4,2]

aTree = BinarySearchTree(6)
bTree = BinarySearchTree(1)
for i in a:
    aTree.insert(i)
for j in b:
    bTree.insert(j)

#aTree.in_order_print(aTree)
bTree.in_order_print(bTree)
