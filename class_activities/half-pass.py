#How do you find and return the middle node of a singly linked list in one pass? You do not have access to the length of the list. If the list is even, you should return the first of the two "middle" nodes. You may not store the nodes in another data structure.
"""
2 pointers: 'half', and 'whole'.
while whole.next != tail:
    half = half.next()
    whole = whole.next().next()
return half
"""

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
