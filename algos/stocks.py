#!/usr/bin/env python
import unittest
import sys

class Solution():
  def stocks(self,prices):
    """ Given a list of integers identify the difference between the lowest and highest values when traversing left to right.
    Assume the values are fluctuation stock prices.  The greatest difference would be the maximized profit.
    Constraint: there is not short-selling. I.e. you must buy before you sell. """
    max_diff = 0
    starting_min = sys.maxsize
    for n in prices:
      if n < starting_min:
        starting_min = n
      elif n - starting_min > max_diff:
        max_diff = n - starting_min
    return max_diff

class Test(unittest.TestCase):
  def test_stocks(self):
    ts = Solution()
    stock_prices = [10, 7, 5, 8, 11, 9]
    max_diff = ts.stocks(stock_prices)
    self.assertEqual(max_diff, 6)
    stock_prices = [10, 7, 3, 5, 8, 11, 3, 9]
    max_diff = ts.stocks(stock_prices)
    self.assertEqual(max_diff, 8)
    stock_prices = [10, 7, 3]
    max_diff = ts.stocks(stock_prices)
    self.assertEqual(max_diff, 0)
    pass

if __name__ == '__main__':
  unittest.main()
