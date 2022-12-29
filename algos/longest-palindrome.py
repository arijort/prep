#!/usr/bin/env python
import unittest

class Solution():
  def longestPalindrome(self, s:str) -> str:
    max_length = 0
    result = ""
    if not s: return result
    if len(s) == 1: return s
    def expand_from_core(st, left, right):
      l, r = left, right
      while 0 <= l and r < len(st) and st[l] == st[r]:
        l -= 1
        r +=1
      return r - l - 1
    for i, ch in enumerate(s):
      local_max = 0
      cand1 = expand_from_core(s, i, i)
      cand2 = expand_from_core(s, i, i+1)
      local_max = max(cand1, cand2)
      if local_max > max_length:
        result = s[ i - (local_max -1) // 2 : i +1 + local_max // 2]
        max_length = local_max
    return result

class Test(unittest.TestCase):
  def test_foo(self):
    ts = Solution()
    self.assertEqual(ts.longestPalindrome("babad"), "bab")
    self.assertEqual(ts.longestPalindrome("cbbd"), "bb")
    self.assertTrue(True)
    pass

if __name__ == '__main__':
  unittest.main()
