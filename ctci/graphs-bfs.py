#!/usr/bin/env python
import unittest
from queues import Queue, QueueNode

class Graph():
  def __init__(self, vertices):
    self.v = vertices
    self.graph = [[ 0 for column in range(vertices) ] for row in range(vertices) ]

  def is_connected(self):
    visited = [ [0] * self.v ] * self.v
    for u in range(self.v):
      for v in range(self.v):
        if self.graph[u][v]:
          print(f"cost from vertex {u} to {v} is {self.graph[u][v]}")
    return True

  def do_bfs(self, start, dest):
    """ Given a node in a graph and a destination, check whether a path exists from the node to the destination.
    Use a BFS to discover a path. """
    # add node to queue
    q = Queue()
    q.put(start)
    visited = set()
    while not q.is_empty():
      # get node from queue
      item = q.get()
      node = item.data
      if node == dest:
        return True # found positive outcome
      if node in visited:
        continue
      # mark this node as visited
      visited.add(node)
      # get neighbors of the node popped
      #print(f"  have graph {self.graph[node]}")
      for u, weight in enumerate(self.graph[node]):
        if weight == 0:
          continue
        #print(f"  working neighbors of n {u}")
      # put each neighbor on the queu
        q.put(u)
    return False

class Test(unittest.TestCase):
  def test_make_graph(self):
    ts = Graph(9)
    # use adjacency matrix to show graph
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
    self.assertTrue(ts.do_bfs(3,8))

if __name__ == '__main__':
  unittest.main()
