#!/usr/bin/env python
import unittest

class Graph():
  def __init__(self, vertices):
    self.v = vertices
    self.graph = [[ 0 for column in range(vertices) ] for row in range(vertices) ]

  def is_connected(self):
    visited = [ [0] * self.v ] * self.v
    print(visited)
    for u in range(self.v):
      for v in range(self.v):
        if self.graph[u][v]:
          print(f"cost from vertex {u} to {v} is {self.graph[u][v]}")

    return True

class Test(unittest.TestCase):
  def test_make_graph(self):
    ts = Graph(9)
    ts.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                [4, 0, 8, 0, 0, 0, 0, 11, 0],
                [0, 8, 0, 7, 0, 4, 0, 0, 2],
                [0, 0, 7, 0, 9, 14, 0, 0, 0],
                [0, 0, 0, 9, 0, 10, 0, 0, 0],
                [0, 0, 4, 14, 10, 0, 2, 0, 0],
                [0, 0, 0, 0, 0, 2, 0, 1, 6],
                [8, 11, 0, 0, 0, 0, 1, 0, 7],
                [0, 0, 2, 0, 0, 0, 6, 7, 0]
                ];

    self.assertTrue(ts.is_connected())
    self.assertTrue(True)

if __name__ == '__main__':
  unittest.main()
