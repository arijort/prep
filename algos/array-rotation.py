#!/usr/bin/env python
import unittest
from pprint import pprint

class Solution():
  def rotleft(self, a, d):
    r=[]
    for i in range(len(a)):
      r.append(  a[ (i + d) % len(a) ] )
    return " ".join(r)

class Test(unittest.TestCase):
  def test_rotleft(self):
    arr = "1 2 3 4 5".split()
    rots = 4
    ts = Solution()
    result = ts.rotleft(arr, rots)
    self.assertEqual("5 1 2 3 4", result)

if __name__ == '__main__':
  unittest.main()
