#!/usr/bin/env python
import unittest
import sys
sys.path.append("/Users/arijort/py/prep/algos")
from trees import BinarySearchTreeNode
from LinkedListNode import LinkedListNode


class Solution():
  """ Given a tree in node, create a list of Linked List structures, on for each depth in the tree. """
  def list_of_depths(self,node):
    depths = []
    l = LinkedListNode(node.value)
    depths.append(l)
    self.list_of_depths_util(node.left, 1, depths)
    self.list_of_depths_util(node.right, 1, depths)
    lists = map(lambda x: x.mk_list() , depths)
    result = [ i for i in lists ]
    #[ print(m) for m in result ]
    return result

  def list_of_depths_util(self, node, depth, depths):
    if node == None:
      return
    l = LinkedListNode(node.value)
    if depth > len(depths) - 1:
      depths.append(l)
    else:
      depths[depth].appendNode(l)
    self.list_of_depths_util(node.left, depth + 1, depths)
    self.list_of_depths_util(node.right, depth + 1, depths)
    return

class Test(unittest.TestCase):
  def test_list_of_depths(self):
    ts = Solution()
    tree = BinarySearchTreeNode()
    bst4 = tree.construct_binary_search_tree(list(range(4)))
    bst4.do_traversals()
    lod = ts.list_of_depths(bst4)
    self.assertEqual(list(lod), [[2], [1,3] , [0] ] )
    bst76 = tree.construct_binary_search_tree(list(range(76)))
    bst76.do_traversals()
    ts.list_of_depths(bst76)

    bad_tree = BinarySearchTreeNode()
    [ bad_tree.add_child(i) for i in range(76) ]
    bad_tree.do_traversals()
    bad_lod = ts.list_of_depths(bad_tree)
    self.assertEqual(len(bad_lod), 76) # test that this tree is pathological, i.e. it has a depth of 76 for 76 nodes.

if __name__ == '__main__':
  unittest.main()
