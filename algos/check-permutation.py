#!/usr/bin/env python
import unittest

class Solution():
  def check_permutation(self, x, y):
    """ Given 2 strings, check that the 2 strings are permutations of each other. Return boolean. """
    return sorted(x) == sorted(y)

class Test(unittest.TestCase):
  def test_foo(self):
    ts = Solution()
    t1 = ts.check_permutation("abc", "cab")
    self.assertTrue(t1)
    t2 = ts.check_permutation("abc", "caasdfqsdfb")
    self.assertFalse(t2)
    pass

if __name__ == '__main__':
  unittest.main()
