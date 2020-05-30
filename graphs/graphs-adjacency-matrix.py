#!/usr/bin/env python
import unittest
from collections import defaultdict
import heapq

class Graph():
  """ https://ide.geeksforgeeks.org/9je5j6jJ13
  https://www.geeksforgeeks.org/prims-mst-for-adjacency-list-representation-greedy-algo-6/
  Implement a graph using an adjaceny matrix as the backing representation. """
  def __init__(self,numvertices):
    self.numvertices = numvertices
    self.graph = [ [-1] * numvertices for _ in range(numvertices) ] # create 2d matrix in list of lists
    self.vertex_list = [0] * numvertices # keep list of vertices
    self.vertex_dict = {}  # dictionary of vertices
    self.mstgraph = defaultdict(list)

  def add_edge(self, u, v, cost=1):
    """ Add edge from vertex u to v. """
    print(f"adding edge {u} to {v}")
    #print(f"vertex dict {self.vertex_dict}")
    #print(f"vertex u {self.vertex_dict[u]}")
    #print(f"vertex v {self.vertex_dict[v]}")
    self.graph[self.vertex_dict[u]][self.vertex_dict[v]] = cost
    self.graph[self.vertex_dict[v]][self.vertex_dict[u]] = cost # for a directed graph only add cost for one way

  def add_mst_edge(self, u, v, cost=0):
    """ Add edge for a matrix using integers only for vertices. """
    self.graph[u][v] = cost
    self.graph[v][u] = cost

    new_node = [v, cost]
    self.mstgraph[u].insert(0, new_node ) 
    
    new_node = [u, cost]
    self.mstgraph[v].insert(0, new_node ) 

  def prim_mst(self):
    numvertices = self.numvertices
    key = []
    parent = []
    minheap = heapq()
    
  def add_vertex(self, vertex, id): # using a string id to view the vertex
    if 0 <= vertex < self.numvertices:
      self.vertex_list[vertex] = id
      self.vertex_dict[id] = vertex

  def get_edges(self):
    edges = []
    print(f"graph {self.graph}")
    for u in range(self.numvertices):
      for v in range(self.numvertices):
        if self.graph[u][v] != -1:
          edges.append( (self.vertex_list[u], self.vertex_list[v], self.graph[u][v] ) )
    print( edges )
    return edges

class Test(unittest.TestCase):
  def test_foo(self):
    ts = Graph(6)
    ts.add_vertex(0,'a')
    ts.add_vertex(1,'b')
    ts.add_vertex(2,'c')
    ts.add_vertex(3,'d')
    ts.add_vertex(4,'e')
    ts.add_vertex(5,'f')

    ts.add_edge('a','e',10)
    ts.add_edge('a','c',20)
    ts.add_edge('c','b',30)
    ts.add_edge('b','e',40)
    ts.add_edge('e','d',50)
    ts.add_edge('f','e',60)

#    self.assertEqual([0,1], (ts.get_edges()))
    self.assertTrue(True)

    prim = Graph(9)
    prim.add_vertex(0,'a')
    prim.add_vertex(1,'b')
    prim.add_vertex(2,'c')
    prim.add_vertex(3,'d')
    prim.add_vertex(4,'e')
    prim.add_vertex(5,'f')
    prim.add_vertex(6,'g')
    prim.add_vertex(7,'h')
    prim.add_vertex(8,'i')

    # prim.add_mst_edge(u, v, cost) # edge from u to v with cost 
    prim.add_mst_edge(0, 1, 4)
    prim.add_mst_edge(0, 7, 8)
    prim.add_mst_edge(1, 2, 8)
    prim.add_mst_edge(1, 7, 11)
    prim.add_mst_edge(2, 8, 2)
    prim.add_mst_edge(2, 5, 4)
    prim.add_mst_edge(2, 3, 7)
    prim.add_mst_edge(3, 4, 9)
    prim.add_mst_edge(3, 5, 14)
    prim.add_mst_edge(4, 5, 10)
    prim.add_mst_edge(5, 6, 2)
    prim.add_mst_edge(6, 8, 6)
    prim.add_mst_edge(6, 7, 1)
    prim.add_mst_edge(7, 8, 7)

    prim.get_edges()


if __name__ == '__main__':
  unittest.main()
