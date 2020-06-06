#!/usr/bin/env python
import unittest
from collections import defaultdict,deque

class Solution():
  """ Given a list of equations and values, treat the equations as being in the form A / B = K.  
  Equations are given as a list of lists of strings.   values are given in a list of floats.
  Also Given is a set of queries.  
  Return a list of values (floats) which satisfy the queries given the arithmetic in the set of equations.
  Any query which cannot be satisfied should have a value of -1
  https://leetcode.com/problems/evaluate-division/

  Technique:
    Create a directed, weighted graph where each edge from vertex a to b is weighted with value k. Each edge indicates the relationship a / b = k.
    In order to resolve the equation v / w, where v and w are vertices in the graph, we can traverse the graph, multiplyting the weight of each edge we traverse.
  """
  def calcEquation(self, equations, values, queries):
    result = [] * len(queries)
    graph = defaultdict(list) # example dict { "a": [tuple("b", 2), tuple("d", 4)], "b": [tuple(a, 0.5)]}

    for i, (x,y) in enumerate(equations):
      print(f"enumerating equations {i} eq {x} / {y}")
      graph[x].append( (y, values[i])) # { a: [ ( b,2), (d,4) ] value is a list of tuples
      graph[y].append( (x, 1/values[i]))

    for i, (x,y) in enumerate(queries):
      result.append( self.bfs_with_weights(graph, x, y) )
    return result

  def bfs_with_weights(self, graph, source, target):
    if source not in graph or target not in graph:
      return -1
    q = deque()
    visited = set()
    q.append( (source, 1) ) # insert tuple with node and weight of the edges on the discovered path; because an edge represents multiplication we can start with 1
    while len(q):
      node, weight = q.popleft()
      if node == target:
        return weight # weight is second item in the tuple
      if node in visited:
        continue
      visited.add(node)
      for neighbor, neighbor_weight in graph[node]:
        q.append( (neighbor, weight * neighbor_weight) )
    return -1 # no path exists

class Test(unittest.TestCase):
  def test_division(self):
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
