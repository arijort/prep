#!/usr/bin/env python
import unittest

class Solution():
  """ TODO: implement ImmutableListNode class in order to test. """
  def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
    stack = []
    node = head.getNext()
    if not node:
      return 
    while node:
      stack.append(node)
      node = node.getNext()

    print(f"in betweeen with stack {stack}")
    while stack:
      node = stack.pop()
      node.printValue()


class Test(unittest.TestCase):
  def test_foo(self):
    ts = Solution()

    self.assertTrue(True)
    self.assertEqual( ts.printLinkedListInReverse( [0,-4,-1,3,-5]), [-5,3,-1,-4,0])
    pass

if __name__ == '__main__':
  unittest.main()
