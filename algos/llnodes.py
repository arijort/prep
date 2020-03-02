#!/usr/bin/env python
import unittest
from pprint import pprint as pp
from LinkedListNode import LinkedListNode

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

    llnode = llnode.partition("p") # partitioning creates a new head
    arr = llnode.mk_list()
    self.assertEqual(arr, ['c', 'b', 'bar', 'foo', 'a', 'b', 'zxy', 'z', 'qux', 'zoqpp'] ) # test removeing from the middle

    # Create 2 numbers using linked list nodes for digits.  Head is the least-significant column (ones)
    num1 = LinkedListNode("7") # create 617
    num1.appendToTail("1")
    num1.appendToTail("6")
    self.assertEqual(num1.valuefromLN(), 617)

    num2 = LinkedListNode("5") # create 295
    num2.appendToTail("9")
    num2.appendToTail("2")
    self.assertEqual(num2.valuefromLN(), 295)

    result = num1.addTo(num2) # treat as integers
    self.assertEqual(num1.addTo(num2), 912)

    intnodes = self.intToLN(result)
    arr = intnodes.mk_list()
    self.assertEqual(arr, ['2', '1', '9'])

    palin = LinkedListNode("a")
    b = palin.appendToTail("b")
    b = palin.appendToTail("b")
    a = palin.appendToTail("a")
    self.assertTrue(palin.isPalin())
    a = palin.appendToTail("c")
    self.assertFalse(palin.isPalin())

    intersection = palin.isIntersection(b)
    self.assertEqual(intersection.s, "b")
    intersection = palin.isIntersection(llnode)
    self.assertEqual(intersection, None)

  def intToLN(self, i):
    if i == 0:
      return None
    l = str(i)
    p = LinkedListNode(l[-1]) # pull out ones column
    for n in l[-2::-1]: # work from 2nd column to the end
      p.appendToTail(n)
    return p


if __name__ == '__main__':
  unittest.main()
