#!/usr/bin/env python
import unittest

class Solution():
  def solution(self,A):
    st = set()
    for n in A:
      st.add(n)
    for i in range(1,len(A) + 2):
      if not i in st:
        return i
    return 1

class Test(unittest.TestCase):
  def test_foo(self):
    ts = Solution()


#    [ self.assertTrue( ts.isPalindrome(i) ) for i in trues ]
#    [ self.assertFalse( ts.isPalindrome(i) ) for i in falses ]
    self.assertTrue(True)
    self.assertEqual( ts.solution([1,2,3]), 4)
    self.assertEqual( ts.solution([-1,-3,-5]), 1)
    pass

if __name__ == '__main__':
  unittest.main()
