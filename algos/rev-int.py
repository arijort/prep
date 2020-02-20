#!/usr/bin/env python
import unittest

class Solution:
  def reverse(self, i):
    """ Given an integer, return the integer with digits in reverse order.  E.g. 123 -> 321.  Negatives should be preserved as negatives.  """
    result = 0
    maxint,minint = 2**31, -2**31 - 1
    neg = False
    if i < 0:
      neg = True
      i = abs(i)
    while i > 0:
      result *= 10
      result += i % 10
      i //= 10
    if result > maxint or result < minint:
      return 0
    if neg:
     return -int(result)
    else:
      return int(result)
    
class Test(unittest.TestCase):
  def test_reverse(self):
    print("starting")
    ts = Solution()
    print("test 1 should be 321 : %d" % ts.reverse(123))
    print("test 2 should be 1 : %d" % ts.reverse(1))
    print("test 3 should be -987 : %d" % ts.reverse(-789))
    print("test 4 should be 0 : %d" % ts.reverse(1534236469))

if __name__ == '__main__':
  unittest.main()
