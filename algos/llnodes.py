#!/usr/bin/env python
import unittest
from pprint import pprint as pp

class LinkedListNode():
  next = None;
  s = ""

  def __init__(self, string):
    self.s = string

  def mk_list(self):
    """ Return a list of values in the linked list from the current node to the end. """
    l, n = list(), self
    l.append(self.s)
    while not n.next == None:
      l.append(n.next.s)
      n = n.next
    return l

  def display(self):
    """ Display values in linked-list nodes from this node until the end. Print self then use next to continue recursively. """
    print(f"node: {self.s}")
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
    if self.next == None:
      return False # We are in fact at the end of the list so do nothing.
    self.s = self.next.s
    self.next = self.next.next
    return True

  def remove_dupes(self):
    """ Given an unsorted singly linked list remove any duplicate nodes. As a secondary: can it be done without any additional data structure. """
    st = set()
    n,head = self,self
    print("before dedupe")
    head.display()
    st.add(n.s)
    while not n.next == None:
      if n.next.s in st:
        n.next = n.next.next
      else:
        st.add(n.next.s)
        n = n.next
    return head

  def remove_kth(self, k):
    n, head, ct = self, self, 1
    while not n.next == None:
      ct += 1
      n = n.next
    print(f"found length {ct} will remove node {ct - k}")
    runner = 0
    n = head # reinitialize node pointer
    while runner < ct - k - 1:
      print(f"runner {runner}")
      n = n.next
      runner += 1
    n.next = n.next.next
    self.display()

    return head

  def remove_this(self):
    """ Given pointer to a node in the middle of linked list, remove the current node keeping the rest of the list intact. """


class Test(unittest.TestCase):
  def test_llnodes(self):
    llnode = LinkedListNode("a")
    b = llnode.appendToTail("b")
    a = llnode.appendToTail("a")
    zxy = llnode.appendToTail("zxy")
    z = llnode.appendToTail("z")
    bar = llnode.appendToTail("bar")
    foo = llnode.appendToTail("foo")


    llnode.remove_dupes()
    arr = llnode.mk_list()
    self.assertEqual(arr, ['a', 'b', 'zxy', 'z', 'bar', 'foo']) # test deduping
    llnode.remove_kth(2)
    arr = llnode.mk_list()
    self.assertEqual(arr, ['a', 'b', 'zxy', 'z', 'foo']) # test removeing kth element

    llnode.appendToTail("bar")
    llnode.appendToTail("b")
    llnode.appendToTail("c")
    quz = llnode.appendToTail("quz")
    llnode.appendToTail("qux")
    llnode.appendToTail("zoqpp")
    quz.remove_this()
    arr = llnode.mk_list()
    self.assertEqual(arr, ['a', 'b', 'zxy', 'z', 'foo', 'bar', 'b', 'c', 'qux', 'zoqpp']) # test removeing from the middle

if __name__ == '__main__':
  unittest.main()
