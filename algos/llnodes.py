#!/usr/bin/env python
import unittest
from pprint import pprint as pp

class LinkedListNode():
  next = None;
  s = ""

  def __init__(self, string):
    self.s = string

  def display(self):
    """ Display values in linked-list nodes from this node until the end. Print self then use next to continue recursively. """
    print(self.s)
    if not self.next == None:
      self.next.display()

  def appendToTail(self, s):
    """ Given a string create a new tail node to the linked list referred to by this node. Follow next pointers linearly to find the end, then append. """
    end = LinkedListNode(s)
    n = self
    while not n.next == None:
      n = n.next
    n.next = end
    return end

  def remove_from_middle(self, s):
    """ Given a string, find the node in the current linked list.  """
    pass

class Solution():
  def foo(self):
    pass

class Test(unittest.TestCase):
  def test_llnodes(self):
    ts = Solution()
    llnode = LinkedListNode("a")
    b = llnode.appendToTail("b")
    a = llnode.appendToTail("a")
    zxy = llnode.appendToTail("zxy")
    z = llnode.appendToTail("z")
    bar = llnode.appendToTail("bar")
    foo = llnode.appendToTail("foo")
    llnode.display()
    zxy.display()
    self.assertTrue(True)

if __name__ == '__main__':
  unittest.main()
