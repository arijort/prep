#!/usr/bin/env python
import unittest
from collections import defaultdict
import heapq
import sys

class Graph():
  """ https://www.geeksforgeeks.org/prims-mst-for-adjacency-list-representation-greedy-algo-6/
  Implement a graph using a dictionary and then derive a minimum spanning tree
  """
  def __init__(self,numvertices):
    self.numvertices = numvertices
    self.graph = defaultdict(list)

  def add_edge(self, u, v, cost=0):
    """ Add edge from vertex u to v. """
    print(f"adding edge {u} to {v} cost {cost}")
    new_node = (v, cost)
    self.graph[u].insert(0, new_node) # dict value is tuple (dest, cost)

    new_node = (u, cost)
    self.graph[v].insert(0, new_node)

  def get_edges(self):
    edges = []
    #print(f"graph {self.graph}")
    for item in self.graph:
      for node, cost in  self.graph[item]:
        print(f"path from {item} to {node} cost {cost}")
    return 

  def prim_mst(self):
    # number of vertices
    V = self.numvertices
    # key values to pick min weight edge
    key = []
    # list to store constructed MST
    parent = []
    
    # min heap for set of edges under consideration
    min_heap = [(0,0) ] # initialize to use 0 as starting vertex with 0 weight

    for v in range(V):
      parent.append(-1)
      key.append( sys.maxsize )
      if v > 0:
        edge_tup = (key[v], v)
        heapq.heappush(min_heap, edge_tup)

    # make key value of of 0th vertex to be 0 so it is extracted first
    print(f"min_heap is {min_heap}")
    heapq.heapify(min_heap)
    print(f"after min_heap is {min_heap}")
    key[0] = 0

    while len(min_heap) > 0:
      new_heap_node = heapq.heappop(min_heap) # new_heap_node is tuple (weight, vertex)
      u = new_heap_node[1]
      print(f"new heap node is {new_heap_node} u {u}")
      # traverse adjacent vertices of u, get the weight of each edge and update distance values
      for pCrawl in self.graph[u]:
        v = pCrawl[0] # pCrawl is tuple (vertex, weight)
        weight = pCrawl[1]
        print(f" crawl have v {v} weight {weight} compare key {key[v]}")
        if weight < key[v]:
          print(f"setting key[v] {key[v]} to weight {weight}")
          key[v] = weight
          parent[v] = u
          heapq.heappush(min_heap, (weight, v))
          
      print(f"have heap {min_heap}")
      print(f"have keys {key}")
      print(f"have parents {parent}")
        
    print(f"returning {parent}")
    return parent

class Test(unittest.TestCase):
  def test_foo(self):
    ts = Graph(9)

    ts.add_edge(0, 1, 4) 
    ts.add_edge(0, 7, 8) 
    ts.add_edge(1, 2, 8) 
    ts.add_edge(1, 7, 11) 
    ts.add_edge(2, 3, 7) 
    ts.add_edge(2, 8, 2) 
    ts.add_edge(2, 5, 4) 
    ts.add_edge(3, 4, 9) 
    ts.add_edge(3, 5, 14) 
    ts.add_edge(4, 5, 10) 
    ts.add_edge(5, 6, 2) 
    ts.add_edge(6, 7, 1) 
    ts.add_edge(6, 8, 6) 
    ts.add_edge(7, 8, 7) 

    ts.get_edges()
    #self.assertTrue(True)
    ts.prim_mst()

if __name__ == '__main__':
  unittest.main()
