#!/usr/bin/env python
import unittest

class Solution():
  def foo(self):
    pass

class Test(unittest.TestCase):
  def test_foo(self):
    ts = Solution()

    trues = [ 121, 74743892484238794238871367813613267813263127688672136231876231631876317883249783248429834747, 1221, 0, 2222222, 2222222]
    falses = [ 1234, 7474389248423879423887136781361326781326312768, -1221, 10 ]

    [ self.assertTrue( ts.isPalindrome(i) ) for i in trues ]
    [ self.assertFalse( ts.isPalindrome(i) ) for i in falses ]
    self.assertEqual(ts.foo(0), 0)
    self.assertTrue(True)
    pass

if __name__ == '__main__':
  unittest.main()
