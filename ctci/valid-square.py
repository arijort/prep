#!/usr/bin/env python
import unittest

class Solution():
  """ https://leetcode.com/problems/valid-square/ 
  Given a set of coordinates return a boolean indicating whether the 4 points make a valid square.
  Each input point is a 2 integer list e.g. [ 0,1 ] """
  def distance(self,p1,p2):
    """ Given 2 points calcualte the square of the distance between them with pythagorean theorem. """
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

  def validSquare(self, p1, p2, p3, p4):
    points = [p1, p2, p3, p4].sort()
    lengths = [ self.distance(p1,p2), self.distance(p1,p3), self.distance(p1,p4), self.distance(p2,p3), self.distance(p2,p4), self.distance(p3,p4) ]
    lengths.sort()
    return lengths[0] == lengths[1] and lengths[1] == lengths[2] and lengths[2] == lengths[3] and lengths[3] != lengths[4] and lengths[4] == lengths[5]

    
class Test(unittest.TestCase):
  def test_valid_square(self):
    ts = Solution()

    trues = [ [ [0,0], [1,1], [1,0], [0,1] ] ]
    falses = [ [ [0,3], [1,1], [1,0], [0,1] ] ]

    self.assertTrue( ts.validSquare([0,0], [1,1], [1,0], [0,1]) )
    self.assertFalse( ts.validSquare([2,0], [1,1], [1,0], [0,1]) )
    pass

if __name__ == '__main__':
  unittest.main()
