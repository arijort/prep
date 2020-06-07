#!/usr/bin/env python
import unittest
import sys

class Solution():
  def get_different_number(self, arr):
    """ 
    Given an array arr of unique nonnegative integers, implement a function getDifferentNumber that finds the smallest nonnegative integer that is NOT in the array.
    """
    s = set(arr)
    for n in range(sys.maxsize):
      if not n in s:
        return n

class Test(unittest.TestCase):
  def test_foo(self):
    ts = Solution()

    self.assertEqual( ts.get_different_number( [0,1,2,3] ), 4)
    self.assertEqual( ts.get_different_number( [0] ), 1)
    pass

if __name__ == '__main__':
  unittest.main()
