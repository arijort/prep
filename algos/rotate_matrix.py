#!/usr/bin/env python
import unittest
from pprint import pprint

class Solution():
  def rotate_matrix(self, m):
    """ Given a matrix of NxN dimension, rotate it 90 degrees clockwise. """
    result = m.copy()
    for x, row in enumerate(m):
      col = [ i[x] for i in m ]
      result[x] = col[::-1] # reverse col into a row to achieve clockwise rotation
    return result

  def rotate_matrix_ccw(self, m):
    """ Given a matrix of NxN dimension, rotate it 90 degrees counter-clockwise. """
    l = len(m) - 1
    pprint(m)
    result = m.copy()
    for x, row in enumerate(m):
      col = [ i[x] for i in m ]
      result[l-x] = col # column assignment into row
    return result

class Test(unittest.TestCase):
  def test_rotate_matrix(self):
    ts = Solution()
    arr = [ [5, 6, 7, 8, 9], [12, 13, 14, 15, 16], [23, 24, 25, 26, 27], [34, 35, 36, 37, 38], [45, 46, 47, 48, 49] ]
    rot = [ [45, 34, 23, 12, 5], [46, 35, 24, 13, 6], [47, 36, 25, 14, 7], [48, 37, 26, 15, 8], [49, 38, 27, 16, 9] ]
    #mtx = [ [0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0] ]
    r = ts.rotate_matrix(arr)
    #r = ts.rotate_matrix_ccw(arr)
    self.assertEqual(r, rot)

if __name__ == '__main__':
  unittest.main()
