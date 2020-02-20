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
    ts = Solution()
    self.assertEqual(321, ts.reverse(123))
    self.assertEqual(1, ts.reverse(1))
    self.assertEqual(-987, ts.reverse(-789))
    self.assertEqual(0, ts.reverse(1534236469))

if __name__ == '__main__':
  unittest.main()
