#!/usr/bin/env python
import unittest
import math
import sys
import os
from pprint import pprint

##############################

class Solution():
# Complete the hourglassSum function below.
  def hourglassSum(self,arr):
    """ Given a square matrix of integers, find the maximum sum of hourglass shaped figures. """
    maxval = - sys.maxsize - 1
    for row in range(len(arr) - 2):
      for col in range(len(arr) - 2):
        val  = arr[row][col] + arr[row][col+1] + arr[row][col+2] + arr[row+1][col+1] + arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
        if val > maxval:
          maxval = val
    return maxval

  def hourglass(self):
    arr = []
    with open("2dmatrix1") as fh:
      for l in fh:
        arr.append(list(map(int, l.split())))
    return self.hourglassSum(arr)

##############################

  def foo(self):
    pass

class Test(unittest.TestCase):
  def test_hourglass(self):
    ts = Solution()
    result = ts.hourglass()
    self.assertGreater(result, 0)
    pass

if __name__ == '__main__':
  unittest.main()
