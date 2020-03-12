#!/usr/bin/env python
import unittest

class Solution:
  def reverse(self, i):
    """ Given an integer, return the integer with digits in reverse order.  E.g. 123 -> 321.  Negatives should be preserved as negatives.  """
    result, neg = 0, 1
    maxint,minint = 2**31, -2**31 - 1
    if i < 0:
      neg = -1
      i = abs(i)
    while i > 0:
      result *= 10
      result += i % 10
      i //= 10
    if result > maxint or result < minint:
      return 0
    return neg * int(result)

class Test(unittest.TestCase):
  def test_reverse(self):
    ts = Solution()
    self.assertEqual(321, ts.reverse(123))
    self.assertEqual(1, ts.reverse(1))
    self.assertEqual(-987, ts.reverse(-789))
    self.assertEqual(0, ts.reverse(1534236469))
    self.assertEqual(0, ts.reverse(7474389248423879423887136781361326781326312768))

if __name__ == '__main__':
  unittest.main()
