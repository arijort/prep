#!/usr/bin/env python
import unittest
from collections import defaultdict

class Solution():
  def palinperm(self,s):
    """ Given a string, check if the characters can be premuted to form a palindrome. """
    # Check 2 modes: whether string has even or odd number of chars, using case-insensitive logic.
    #   If the string has even number of chars, each char must appear an even number of times; else return false
    #   If the string has odd number of chars, one and only 1 must have an odd number of instances, each other char must appear an even number of times; else return false
    d = defaultdict(int)
    ct = 0
    for _, c in enumerate(s.lower()):
      if not c.isalpha():
        continue # ignore non-alpha chars
      d[c] = ~ d[c] # use bitwise manipulation to track even (0) vs odd (-1)
      ct += 1
    v = d.values()
    if ct % 2 == 0:
      return sum(v) == 0
      # check all values are even
    else:
      return sum(v) == -1
      # check all but one values are even
    return True
  

class Test(unittest.TestCase):
  def test_palinperm(self):
    ts = Solution()
    self.assertTrue(ts.palinperm("t"))
    self.assertTrue(ts.palinperm("tt"))
    self.assertTrue(ts.palinperm("ttt"))
    self.assertTrue(ts.palinperm("tttt"))
    self.assertFalse(ts.palinperm("ttta"))
    self.assertTrue(ts.palinperm("tact Coa"))
    self.assertTrue(ts.palinperm("able was i ere i saw elba"))
    self.assertTrue(ts.palinperm("able was i ere i saw elbar"))
    self.assertFalse(ts.palinperm("tact Coa dbopasdfjasdopfiuasopiufdoaisdjf;anlasdnfbmwqer"))
    self.assertFalse(ts.palinperm("tact Coa dbopasdfjasdopfiuasopiufdoaisdjf;anlasdnfbmwqera"))
    self.assertFalse(ts.palinperm("tact Coa dbo"))
    pass

if __name__ == '__main__':
  unittest.main()
