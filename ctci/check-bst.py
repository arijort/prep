#!/usr/bin/env python
import unittest
import sys

def is_binary_search_tree(tree_root):
    """ Given the root of a tree check if this tree is in fact a binary search tree.
    Use the rule that for each non-leaf node in the tree, the node is greater than the max value of the subtree on the left
    and less than the min value of the subtree on the right. """
    if not tree_root:
        return True
    minint = - sys.maxsize -1
    maxint = sys.maxsize
    return check_in_range(tree_root, minint, maxint)

def check_in_range(node, minval, maxval):
    if not node: # we passed a leaf so return true
        return True
    if node.value < minval or node.value > maxval:
        return False
    left_good, right_good = True, True
    if node.left:
       left_good = check_in_range(node.left, minval, node.value)
       if not left_good:
           return False
    if node.right:
       right_good = check_in_range(node.right, node.value, maxval)
       if not right_good:
           return False
    return True # this is a leaf node so can't check left and right sides

def check_bst_dfs_iter(tree_root):
    print(f"checking tree node {tree_root.value} ")
    if not tree_root:
        return True
    minval, maxval = -float('inf'), float('inf')
    nodes = []
    nodes.append( (tree_root, minval, maxval) )
    while len(nodes):
        node, bottom_end, top_end = nodes.pop()
        print(f"  checking node {node.value} min {bottom_end} top {top_end}")
        if node.value < bottom_end or node.value > top_end:
            return False
        if node.left:
            nodes.append( (node.left, bottom_end, node.value) )
        if node.right:
            nodes.append( (node.right, node.value, top_end) )
    return True

class Test(unittest.TestCase):
    class BinaryTreeNode(object):
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def insert_left(self, value):
            self.left = Test.BinaryTreeNode(value)
            return self.left

        def insert_right(self, value):
            self.right = Test.BinaryTreeNode(value)
            return self.right

    def test_valid_full_tree(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        right.insert_left(60)
        right.insert_right(80)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)
        dfs_result = check_bst_dfs_iter(tree)
        self.assertTrue(dfs_result)

    def test_both_subtrees_valid(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(80)
        left.insert_left(20)
        left.insert_right(60)
        right.insert_left(70)
        right.insert_right(90)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)
        dfs_result = check_bst_dfs_iter(tree)
        self.assertFalse(dfs_result)
"""
     50
  30    80
20 60  70 90
"""
if __name__ == '__main__':
  unittest.main(verbosity=2)

# vi: ts=4
