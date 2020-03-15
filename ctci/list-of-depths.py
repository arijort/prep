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

    trues = [ True, 1 ]
    falses = [ False, 0 ]

    [ self.assertTrue( i ) for i in trues ]
    [ self.assertFalse( i ) for i in falses ]
    self.assertTrue(True)
    pass

if __name__ == '__main__':
  unittest.main()
