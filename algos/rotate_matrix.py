#!/usr/bin/env python
import unittest
from pprint import pprint

class Solution():
  def rotate_matrix(self, m):
    """ Given a matrix of NxN dimension, rotate it 90 degrees clockwise. """
    pprint(m)
    result = m.copy()
    for x, row in enumerate(m):
      col = [ i[x] for i in m ]
      result[x] = col[::-1] # reverse col into a row to achieve clockwise rotation
    print("result array")
    pprint(result)
    return False

  def rotate_matrix_ccw(self, m):
    """ Given a matrix of NxN dimension, rotate it 90 degrees counter-clockwise. """
    l = len(m) - 1
    pprint(m)
    result = m.copy()
    for x, row in enumerate(m):
      col = [ i[x] for i in m ]
      result[l-x] = col # column assignment into row
    print("result array")
    pprint(result)
    return False

class Test(unittest.TestCase):
  def test_rotate_matrix(self):
    ts = Solution()
    arr = [ [5, 6, 7, 8, 9], [12, 13, 14, 15, 16], [23, 24, 25, 26, 27], [34, 35, 36, 37, 38], [45, 46, 47, 48, 49] ]
    #mtx = [ [0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0] ]
    r = ts.rotate_matrix(arr)
    r = ts.rotate_matrix_ccw(arr)
    self.assertTrue(not r is None)

if __name__ == '__main__':
  unittest.main()
