#!/usr/bin/env python
import unittest

class Graph():
  """ Implement a graph without specifying directedness. """
  def __init__(self):
    self.nodes = set()
    self.labels = set()
    self.adj_list = []
    self.adj_matrix = []

  def add_node(self, node):
    self.nodes.add(node)

  def create_graph_from_adjancency_list(self, adj_list):
    """ Given a list of lists, regard each item in the list as the list of neighbors for that node. """
    if not adj_list:
      return
    self.adj_list = adj_list

  def visit_nodes_by_list(self):
    for u in range(len(self.adj_list)):
      if not self.adj_list[u]:
        continue
      for v in range(len(self.adj_list[u])):
        print(f"showing edge from node {u} to {self.adj_list[u][v]}")
    return

  def create_graph_from_matrix(self, matrix):
    """ Given a matrix of values, create non-directed graph edges between nodes at each coordinate with a non-zero value.
    In a future implementation use the value as the weight of the graph. """
    if not matrix:
        return
    self.adj_matrix = matrix

  def visit_nodes_by_matrix(self):
    for u in range(len(self.adj_matrix)):
      for v in range(len(u)):
        if self.adj_matrix[u][v]:
          print(f"showing edge from node {u} to {v}")
    return

class DirectedGraphNode():
    """ Implementation of a node in a directed graph """
    def __init__(self, label):
        self.label = label
        self.paths_to = set() # set of nodes where we can follow a path from self to nodes

    def add_path_to(self, label):
        new_node = DirectedGraphNode(label)
        self.paths_to.add(new_node)

class GraphNode:
    """ Implementation of a single node in a graph """
    def __init__(self, label):
        self.label = label
        self.neighbors = set()

    def add_neighbor(self, node):
        """ Add the node given with node as a neighbor. Assume it is already a GrapheNode instance. """
        self.neighbors.add(node)

class Test(unittest.TestCase):
  def test_make_graph(self):
    ts = Graph()
    graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                [4, 0, 8, 0, 0, 0, 0, 11, 0],
                [0, 8, 0, 7, 0, 4, 0, 0, 2],
                [0, 0, 7, 0, 9, 14, 0, 0, 0],
                [0, 0, 0, 9, 0, 10, 0, 0, 0],
                [0, 0, 4, 14, 10, 0, 2, 0, 0],
                [0, 0, 0, 0, 0, 2, 0, 1, 6],
                [8, 11, 0, 0, 0, 0, 1, 0, 7],
                [0, 0, 2, 0, 0, 0, 6, 7, 0]
                ];
    ts.create_graph_from_matrix(graph)
    adj_list = [ [], [2, 5], [1,5,3,4], [2, 4], [2, 5, 3], [4, 1, 2] ]
    ts.create_graph_from_adjancency_list(adj_list)
    ts.visit_nodes_by_list()

    binary_tree_7_list = [ [1,2], [0,3,4], [0,5,6], [1], [1], [2], [2] ]
    gr = Graph()
    gr.create_graph_from_adjancency_list(binary_tree_7_list)
    gr.visit_nodes_by_list()
    binary_tree_7_matrix = [[ 0, 1, 1, 0, 0, 0, 0],
                            [ 1, 0, 0, 1, 1, 0, 0],
                            [ 1, 0, 0, 0, 0, 1, 1],
                            [ 0, 1, 0, 0, 0, 0, 0],
                            [ 0, 1, 0, 0, 0, 0, 0],
                            [ 0, 0, 1, 0, 0, 0, 0],
                            [ 0, 0, 1, 0, 0, 0, 0]]
    self.assertTrue(True)

if __name__ == '__main__':
  unittest.main()
