#!/usr/bin/env python
import unittest
from trees import BinarySearchTreeNode

class Solution:
    """ from Interview Cake """
    def compute_depth(self, node: BinarySearchTreeNode) -> int:
        """ Return tree depth in O(d) time.  """
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d

    def exists(self, idx: int, d: int, node: BinarySearchTreeNode) -> bool:
        """ Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).  Return True if last level node idx exists.  Binary search with O(d) complexity.  """
        left, right = 0, 2**d - 1
        print(f"  checking exists with idx {idx} d {d} node {node.value}")
        for _ in range(d):
            pivot = left + (right - left) // 2
            print(f"    checking pivot {pivot} in left {left} right {right}")
            if idx <= pivot:
                print(f"      going left")
                node = node.left
                right = pivot
            else:
                print(f"      going right")
                node = node.right
                left = pivot + 1
        print(f"    ret { node is not None}")
        return node is not None

    def countNodes(self, root: BinarySearchTreeNode) -> int:
        # if the tree is empty
        if not root:
            return 0
        d = self.compute_depth(root)
        print(f"have depth {d}")
        # if the tree contains 1 node
        if d == 0:
            return 1
        # Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        # Perform binary search to check how many nodes exist.
        left, right = 1, 2**d - 1
        while left <= right:
            pivot = left + (right - left) // 2
            print(f"  searching on pivot {pivot}")
            if self.exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1
        # The tree contains 2**d - 1 nodes on the first (d - 1) levels
        # and left nodes on the last level.
        print(f"finished with left {left}")
        return (2**d - 1) + left

class Test(unittest.TestCase):
  def test_foo(self):
    ts = Solution()
    tr76 = [ i * 10 for i in range(76) ]
    tree = BinarySearchTreeNode()
    bst76 = tree.construct_binary_search_tree(tr76)
    self.assertEqual(76,ts.countNodes(bst76))


if __name__ == '__main__':
  unittest.main()
# vi: ts=4
