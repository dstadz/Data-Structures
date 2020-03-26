#How do you reverse a singly linked list without recursion? You may not store the list, or it's values, in another data structure.


class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
