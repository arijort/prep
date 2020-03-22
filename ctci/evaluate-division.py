#!/usr/bin/env python
import unittest

class Solution():
  """ Given a list of equations and values, treat the equations as being in the form A / B = K.  
  Equations are given as a list of lists of strings.   values are given in a list of floats.
  Also Given is a set of queries.  
  Return a list of values (floats) which satisfy the queries given the arithmetic in the set of equations.
  Any query which cannot be satisfied should have a value of -1
  https://leetcode.com/problems/evaluate-division/ """
  #def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]
  def calcEquation(self, equations, values, queries):
    queries_len = len(queries)
    return [ -1 ] * queries_len



class Test(unittest.TestCase):
  def test_foo(self):
    ts = Solution()
    equations = [ ["a", "b"], ["b", "c"] ]
    values = [2.0, 3.0]
    queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
    expected = [6.0, 0.5, -1.0, 1.0, -1.0 ]
    result = ts.calcEquation( equations, values, queries )
    self.assertEqual(expected,result)
    pass

if __name__ == '__main__':
  unittest.main()
