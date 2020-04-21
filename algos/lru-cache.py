#!/usr/bin/env python
import unittest

class Solution():
  """ Implement an LRU cache. 
  Required methods are get and set.  Aim for O(1) time for both methods. """
  def __init__(self, capacity):
    """ TODO: implement using OrderedDict in collections """
    self.cache = {} # hash value will be a tuple including given value and sequence number
    self.latest_seq = 0
    self.capacity = capacity

  def get(self, key):
    if not key in self.cache:
      return -1 
    if self.cache[key][1]
  def set(self, key, value):
    self.latest_seq += 1
    self.cache[key] = (value, self.latest_seq)

class Test(unittest.TestCase):
  def test_foo(self):
    ts = Solution()

    trues = [ 121, 74743892484238794238871367813613267813263127688672136231876231631876317883249783248429834747, 1221, 0, 2222222, 2222222]
    falses = [ 1234, 7474389248423879423887136781361326781326312768, -1221, 10 ]

    [ self.assertTrue( ts.isPalindrome(i) ) for i in trues ]
    [ self.assertFalse( ts.isPalindrome(i) ) for i in falses ]
    self.assertTrue(True)
    pass

if __name__ == '__main__':
  unittest.main()
