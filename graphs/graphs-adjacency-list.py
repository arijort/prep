#!/usr/bin/env python
import unittest

class Graph():
  """ https://practice.geeksforgeeks.org/problems/print-adjacency-list/0
  Given a set of edges and vertices create the adjacency list for the graph. """
  def __init__(self,numvertices):
    self.numvertices = numvertices
    self.adj_list = [ [] for _ in range(numvertices) ]

  def add_edge(self, u,v ):
    """ Add and edge to the graph from vertex u to vertex v."""
    if u >= self.numvertices or v >= self.numvertices:
      return
    self.adj_list[u].append(v)
    self.adj_list[v].append(u)

  def show_graph(self):
    for vertex, adjacents in enumerate(self.adj_list):
      print(f"vertex {vertex}")
      print(self.adj_list[vertex])

class Test(unittest.TestCase):
  def test_foo(self):
    tg = Graph(5)
    tg.add_edge(0,1)
    tg.add_edge(0,4)
    tg.add_edge(1,2)
    tg.add_edge(1,3)
    tg.add_edge(1,4)
    tg.add_edge(2,3)
    tg.add_edge(3,3)
    tg.add_edge(3,4)

    tg.show_graph()

    self.assertTrue(True)

if __name__ == '__main__':
  unittest.main()
