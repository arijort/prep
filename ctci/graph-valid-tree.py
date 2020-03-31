#!/usr/bin/env python
import unittest
import typing
import collections

class UnionFind():
  def __init__(self,n):
    # make an array for each given edge
    self.parent = [ node for node in range(n)]

  def find(self,A):
    """ Find root of A in the set """
    while A != self.parent[A]:
      A = self.parent[A]
    return A
  def union(self,A, B):
    """ Merge sets A and B by pointing B to A's root. Return false if we did not merge sets. """
    rootA = self.find(A)
    rootB = self.find(B)
    if rootA == rootB:
      return False
    self.parent[rootB] = rootA
    return True


class GraphNode():
  def __init__(self,node):
    self.node = node
    self.neighbors = set()

  def add_neighbor(self,neighbor):
    self.neighbors.add(neighbor)

class Solution():
  """ https://leetcode.com/problems/graph-valid-tree/
  Given a graph in the form of an adjacency list determine whether this graph constitutes a valid tree.
  Check by looking for a cycle. """
  def graph_valid_tree_union_find(self, nodes: int, edges ) -> bool:
    if len(edges) != nodes -1: return False
    union_find = UnionFind(nodes)
    return all( [  union_find.union(A,B) for A, B in edges] )


  def graph_valid_tree(self, nodes: int, edges ) -> bool:
    if len(edges) != nodes - 1: return False
    print(f"len {len(edges)} n is {nodes})")
    adj_list = [ [] for _ in range(nodes)]
    for A,B in edges:
      adj_list[A].append(B)
      adj_list[B].append(A)

    print(adj_list)
    # check if all nodes are connected
    seen = set()
    # use map of parent
    #parent = { 0: -1 } # maps from node to "parent" it was discovered from
    #stack = [0]

    def do_iterative_dfs( stack, parent ):
      while stack:
        node = stack.pop()
        for neighbor in adj_list[node]:
          if neighbor == parent[node]:
            continue
          if neighbor in parent:
            return False
          parent[neighbor] = node
          print(f"appending neighbor {neighbor} ")
          stack.append(neighbor)
      return True
    #return do_iterative_dfs( [0], {0:-1})

    def do_bfs(start,target):
      queue = collections.deque([0])
      seen = set([0])
      while queue:
        n = queue.popleft()
        for neighbor in adj_list[n]:
          if neighbor not in seen:
            print(f"appending neighbor {neighbor}")
            queue.append(neighbor)
            seen.add(neighbor)
      return len(seen) == target

    return do_bfs(0, nodes)


  def check_cycle_dfs(self,node,cycle_check_seen):
    print(f"node is {node} with seen {cycle_check_seen}" )
    if node in cycle_check_seen:
      return False # false means we found a cycle thus graph is not a tree
    cycle_check_seen.add(node)
    found_cycles = [ self.check_cycle_dfs(neighbor, cycle_check_seen) for neighbor in node.neighbors]
    return all(found_cycles) # true means no cycle


class Test(unittest.TestCase):
  def get_falses(self):
    return [ (6, [[0,1], [1,2], [2,3], [1,3], [1,4]] ) ]
  def get_trues(self):
    return [ (5, [[0,1], [0,2], [0,3], [1,4]]) ]
  def test_graph_valid_tree_union_find(self):
    ts = Solution()
    [ self.assertTrue( ts.graph_valid_tree_union_find(n, e) ) for n, e in self.get_trues() ]
    [ self.assertFalse( ts.graph_valid_tree_union_find(n, e) ) for n, e in self.get_falses() ]
  def test_graph_valid_tree(self):
    ts = Solution()
    [ self.assertTrue( ts.graph_valid_tree(n, e) ) for n, e in self.get_trues() ]
    [ self.assertFalse( ts.graph_valid_tree(n, e) ) for n, e in self.get_falses() ]

if __name__ == '__main__':
  unittest.main(verbosity=2)
