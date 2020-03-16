#!/usr/bin/env python
import unittest
from collections import defaultdict

class Solution():
  def __init__(self):
    self.d = dict()

  def logger_limiter(self, timestamp, message):
    result = message not in self.d or timestamp >= self.d[message] + 10
    if result:
      self.d[message] = timestamp
    return result

class Test(unittest.TestCase):
  def test_logger_limiter(self):
    ts = Solution()

    trues = [ (1, "foo"), (2, "bar"), (11, "foo") ]
    falses = [ (3, "foo"), (8, "bar"), (10, "foo")  ]

    #[ self.assertTrue( ts.logger_limiter(t, m) ) for t, m in trues ]
    #[ self.assertFalse( ts.logger_limiter(t, m) ) for t, m in falses ]

    self.assertTrue( ts.logger_limiter(1, "foo"))
    self.assertTrue( ts.logger_limiter(2, "bar"))
    self.assertFalse(ts.logger_limiter(3, "foo"))
    self.assertFalse(ts.logger_limiter(8, "bar"))
    self.assertFalse(ts.logger_limiter(10, "foo"))
    self.assertTrue(ts.logger_limiter(11, "foo"))

if __name__ == '__main__':
  unittest.main()
