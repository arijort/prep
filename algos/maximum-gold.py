#!/usr/bin/env python
import unittest
from typing import List
import math
from pprint import pprint as pp

class Solution():
  """ https://leetcode.com/problems/path-with-maximum-gold/
  https://leetcode.com/problems/path-with-maximum-gold/discuss/551232/Python
  Given a graph of integers, find the path through the graph with maximum integer sum.  
  The path must include only non-zero nodes and cardinal directions. """
  def getMaximumGold(self, g: List[List[int]]) -> int:
    for i in range(len(g)):
      pp(g[i])
    all_values = [self.dfs(i, j, g, set()) for i in range(len(g)) for j in range(len(g[0]))]
    pp(all_values)
    values = [ t[0] for t in all_values ]
    return max(values)
    
  def dfs(self, i, j, g, visited):
    #print(f"doing dfs at {i}, {j} and visited {visited}")
    if not (0 <= i < len(g) and 0 <= j < len(g[0]) and g[i][j] != 0 and (i,j) not in visited):
      #print(f"  bad square")
      return (-math.inf, [-math.inf] )
    #print(f"val {g[i][j]}")
    #pp(g)
    visited.add((i, j))
    node_list = [g[i][j]]
    candidate_values = [ self.dfs(i+x, j+y, g, visited) for x,y in [[-1, 0], [1, 0], [0, 1], [0, -1]]]
    pp(candidate_values)
    #values = [ t[0] for t in candidate_values ]
    max_value = 0
    for candidate in candidate_values:
      max_cand = candidate[0]
      values = candidate[1]
      if max_cand > max_value:
        max_value = max_cand
        [ node_list.append(i) for i in values]
    res = g[i][j] + max(0, max_value)
    #print(f"  have tentative result {res}")
    visited.remove((i, j))
    print(f"node_list {node_list}")
    return (res, node_list)

class Test(unittest.TestCase):
  def test_foo(self):
    ts = Solution()

    grid1 = [[0,6,0],[5,8,7],[0,9,0]]
    self.assertEqual(ts.getMaximumGold(grid1), 24)
    grid2 = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
    self.assertEqual(ts.getMaximumGold(grid2), 28)
    grid3 = [[1,0,7,0,0,0],[2,0,6,0,1,0],[3,5,6,7,4,2],[4,3,1,0,2,0],[3,0,5,0,20,0]]
    self.assertEqual(ts.getMaximumGold(grid3), 60)

if __name__ == '__main__':
  unittest.main()
