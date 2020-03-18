#!/usr/bin/env python
import unittest
import sys
from math import ceil,log

class TreeNode():
  """ Generic node class for trees. """
  def __init__(self,v):
    self.children = []
    self.value = v

  def visit(self, l):
    #print(self.value)
    l.append(self.value)

  def add_child(self,v):
    n = TreeNode(v)
    self.children.append(n)

class BinarySearchTreeNode(TreeNode):
  def __init__(self,v=None):
    self.children = [None] * 2
    self.left = None
    self.right = None
    self.value = v

  def add_child(self, v):
    if self.value is None:
      self.value = v
    elif v < self.value: # go left
      if self.left == None:
        self.left = BinarySearchTreeNode(v)
      else:
        self.left.add_child(v)
    else: # go right
      if self.right == None:
        self.right = BinarySearchTreeNode(v)
      else:
        self.right.add_child(v)

  def visual_visit(self, d):
    print(f"depth {d} node: {self.value}")

  def do_pre_order_traversal_visual(self,d):
    self.visual_visit(d)
    if self.left != None:
      self.left.do_pre_order_traversal_visual(d+1)
    if self.right != None:
      self.right.do_pre_order_traversal_visual(d+1)

  def do_in_order_traversal(self,l):
    if self.left != None:
      self.left.do_in_order_traversal(l)
    self.visit(l)
    if self.right != None:
      self.right.do_in_order_traversal(l)
    return l

  def do_pre_order_traversal(self,l):
    if not l:
      l = []
    self.visit(l)
    if self.left != None:
      self.left.do_pre_order_traversal(l)
    if self.right != None:
      self.right.do_pre_order_traversal(l)
    return l

  def do_post_order_traversal(self,l):
    if not l:
      l = []
    if self.left != None:
      self.left.do_post_order_traversal(l)
    if self.right != None:
      self.right.do_post_order_traversal(l)
    self.visit(l)
    return l

  def do_traversals(self):
    iotl,preotl,postotl= [], [], []
    self.do_in_order_traversal(iotl)
    print(f"in-order traversal {iotl}")
    self.do_pre_order_traversal(preotl)
    print(f"pre-order traversal {preotl}")
    self.do_post_order_traversal(postotl)
    print(f"post-order traversal {postotl}")
    #self.do_pre_order_traversal_visual(0)

  def get_h_from_n(self,n):
    """ Given a number of nodes n, return the height of a balanced binary search tree of n nodes. """
    return ceil(log(n+1,2))

  def get_num_lowest_leaves_from_n(self,n):
    """ Given a number of nodes n, compute how many leaf nodes would be in the bottom row of a perfectly balanced binary search tree. """
    return 1 + n - ( 2 ** int(log(n,2)))

  def construct_binary_search_tree(self,l):
    return self.construct_binary_search_tree_util(l)

  def construct_binary_search_tree_util(self,l):
    """ Given a list of sorted integers, use the list as an in-order traversal of a tree and reconstruct the minimal height tree.
    This is done by recursively finding the optimal rootnode, splitting the elements into left and right halves and creating a BST from each. """
    ##print(f"working list len {len(l)} {l}")
    if len(l) == 0:
      return None
    height = self.get_h_from_n(len(l))
    ##print(f"  have height {height}")
    num_leafs_in_bottom = self.get_num_lowest_leaves_from_n(len(l))
    #print(f"  have num_leafs_in_bottom {num_leafs_in_bottom}")
    if num_leafs_in_bottom >= 2 ** (height - 2): # if left half of bottom row is full
      rootidx = int(2 ** (height - 1)) - 1
    else: # left half of bottom row is not full
      rootidx = int(2 ** (height - 2)) + num_leafs_in_bottom -1
    #rootidx = max( int(2 ** (height - 1)) - 1, int(2 ** (height - 2)) + num_leafs_in_bottom -1 )
    #print(f"  start from node {l[rootidx]}")
    rootnode = BinarySearchTreeNode(l[rootidx])

    # for all non-leaf nodes, construct the left and right pointers
    if height > 1:
      lefttree = self.construct_binary_search_tree(l[0:rootidx])
      righttree = self.construct_binary_search_tree(l[rootidx+1:])
      rootnode.left = lefttree
      rootnode.right = righttree

    return rootnode

  def check_min_depth(self, node, depth):
    """ Given a node, find the maximum depth from that node down to a leaf node. """
    if node.left is None or node.right is None:
      return depth
    return min( self.check_min_depth(node.left, depth + 1), self.check_min_depth(node.right, depth + 1))

  def check_max_depth(self, node, depth):
    """ Given a node, find the maximum depth from that node down to a leaf node. """
    max_left, max_right = 0,0
    if node.left is not None:
      max_left = self.check_max_depth(node.left, depth + 1)
    if node.right is not None:
      max_right = self.check_max_depth(node.right, depth + 1)
    return max(depth, max_left, max_right)

  def check_depth_for_balance(self, node):
    if node is None:
      return -1
    minint = - sys.maxsize - 1
    ld = self.check_depth_for_balance(node.left)
    if ld == minint:
      return minint
    rd = self.check_depth_for_balance(node.right)
    if rd == minint:
      return minint
    if abs(ld - rd) > 1:
      return - sys.maxsize - 1
    return max(ld , rd) + 1

  def is_balanced(self):
    """ Check whether this tree is balanced, i.e. the depth of each leaf node differs by no more than one. """
    return self.check_depth_for_balance(self) != - sys.maxsize - 1

  def validate_bst(self):
    """ validate if the current tree is in fact a binar search tree. """
    return self.validate_bst_util(self, - sys.maxsize -1, sys.maxsize)

  def validate_bst_util(self, node, rangemin, rangemax):
    if node is None:
      return True
    if node.value < rangemin or node.value > rangemax:
      return False
    left_check  = self.validate_bst_util(node.left, rangemin, node.value)
    right_check = self.validate_bst_util(node.right, node.value, rangemax)
    return left_check and right_check

class Tree():
  """ Tree class likely won't be used but this is a stub for it. """
  def __init__(self):
    self.root = TreeNode()
class Test(unittest.TestCase):
  def test_trees(self):
    ts = BinarySearchTreeNode(5)
    array = [ 4,3,5,2,6,7 ]
    for i in array:
      ts.add_child(i)
    ts.do_traversals()
    self.assertTrue(True)
    trl1 = list(range(12))
    trl2 = list(range(76))
    self.assertEqual( ts.get_num_lowest_leaves_from_n(len(trl1)), 5)
    self.assertEqual( ts.get_h_from_n(len(trl1)), 4)
    self.assertEqual( ts.get_num_lowest_leaves_from_n(len(trl2)), 13)
    self.assertEqual( ts.get_h_from_n(len(trl2)), 7)

    tree = BinarySearchTreeNode()
    bst = tree.construct_binary_search_tree(trl2)
    bst.do_traversals()
    bst4 = tree.construct_binary_search_tree(list(range(4)))
    bst4.do_traversals()

    bst100 = tree.construct_binary_search_tree(list(range(100)))
    bst100preot = bst100.do_pre_order_traversal([])
    bst100iot =   bst100.do_in_order_traversal([])
    print(f"bst100 pre-order is {bst100preot}")
    self.assertEqual( bst100iot, list(range(100)) )
    newbst100 = BinarySearchTreeNode()
    # test that recreating a tree via insert-only using a pre order traversal will create the same tree
    [ newbst100.add_child(i) for i in bst100preot ]
    new100 = newbst100.do_pre_order_traversal([])
    self.assertEqual( bst100preot, new100)

    """ Interesting points to note:
      * adding a stream of integers to a tree rooted at the initial integer will likely give a badly balanced tree
      * take a sorted list of integers and derive a minimal complete tree by choosing the right root node in construct_binary_search_tree()
      * the pre-order traversal can be used to reconstitue a tree smiply by adding thoe integers back into the tree.
    """

if __name__ == '__main__':
  unittest.main()
  """
  each full layer brings tree to 2^k - 1 total nodes.  E.g. with 3 layers we have 7 total nodes.
  k = 3 : n = 7 [0, 1, 2, 3, 4, 5, 6]
      3       0 2 4 6
    1   5     \1/ \5/
   0 2 4 6      \3/

   k = 4, n=8
       4
     2   6
    1 3 5 7
   0
   k = 4, n=9 [0, 1, 2, 3, 4, 5, 6, 7, 8]
       5
     3   6
    1 4 7 8
   0 2
   k = 4, n=10 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        6
     3    8
   1   5 7 9
  0 2 4
   k = 4, n=11 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        7
    3     9
  1   5  8 10
 0 2 4 6
   k = 4, n=12 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        7
    3     10
  1   5   9  11
 0 2 4 6 8
   k = 4, n=13 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        7
    3      11
  1   5   9  12
 0 2 4 6 8 10
   k = 4, n=14 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        7
    3      11
  1   5   9    13
 0 2 4 6 8 10 12
   k = 4, n=15 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        7
    3      11
  1   5   9    13
 0 2 4 6 8 10 12 14



 height 6
 row 1 1
 row 2 2
 row 3 4
 row 4 8
 row 5 16
 row 6 14
 """

