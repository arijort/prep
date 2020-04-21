#!/usr/bin/env python
import unittest

# Definition for a Node.
class Node:
  def __init__(self, val, prev, next, child):
    self.val = val
    self.prev = prev
    self.next = next
    self.child = child

class Solution():
  """ https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
  Given a linked list structure where some nodes have a "child" linked list, return a flattened list.
  """
  def flatten(self, head):
    level_start = head
    return self.flattener_helper(level_start)

  def flattener_helper(self,start_node):
    result = []
    runner = start_node
    while runner:
      result.append(start_node.val)
      if runner.child:
        result = result + self.flattener_helper(runner)
      runner = runner.next
    return result


class Test(unittest.TestCase):
  def test_foo(self):
    ts = Solution()
    # This is incomplete

if __name__ == '__main__':
  unittest.main()
