#!/usr/bin/env python
import unittest
import cProfile
from collections import defaultdict

class Solution():
  def ctci_palinperm(self,phrase):
      '''function checks if a string is a permutation of a palindrome or not'''
      """ profile results 5438 function calls (5395 primitive calls) in 0.004 seconds """
      table = [0 for _ in range(ord('z') - ord('a') + 1)]
      countodd = 0
      for c in phrase:
          x = self.char_number(c)
          if x != -1:
              table[x] += 1
              if table[x] % 2:
                  countodd += 1
              else:
                  countodd -= 1
      return countodd <= 1
  def char_number(self,c):
      a = ord('a')
      z = ord('z')
      A = ord('A')
      Z = ord('Z')
      val = ord(c)
      if a <= val <= z:
          return val - a
      elif A <= val <= Z:
          return val - A
      return -1

  def palinperm(self,s):
    """ Given a string, check if the characters can be premuted to form a palindrome. """
    """ profile results: 4423 function calls (4380 primitive calls) in 0.004 seconds """
    # Check 2 modes: whether string has even or odd number of chars, using case-insensitive logic.
    #   If the string has even number of chars, each char must appear an even number of times; else return false
    #   If the string has odd number of chars, one and only 1 must have an odd number of instances, each other char must appear an even number of times; else return false
    d = defaultdict(int)
    for _, c in enumerate(s.lower()):
      if not c.isalpha():
        continue # ignore non-alpha chars
      d[c] = ~ d[c] # use bitwise manipulation to track even (0) vs odd (-1)
    return sum(d.values()) >= -1

class Test(unittest.TestCase):
  def test_palinperm(self):
    ts = Solution()
    self.assertTrue(ts.palinperm("t"))
    self.assertTrue(ts.palinperm("tt"))
    self.assertTrue(ts.palinperm("ttt"))
    self.assertTrue(ts.palinperm("tttt"))
    self.assertFalse(ts.palinperm("ttta"))
    self.assertTrue(ts.palinperm("tttat"))
    self.assertTrue(ts.palinperm("tact Coa"))
    self.assertTrue(ts.palinperm("able was i ere i saw elba"))
    self.assertTrue(ts.palinperm("able was i ere i saw elbar"))
    self.assertFalse(ts.palinperm("tact Coa dbopasdfjasdopfiuasopiufdoaisdjf;anlasdnfbmwqer"))
    self.assertFalse(ts.palinperm("tact Coa dbopasdfjasdopfiuasopiufdoaisdjf;anlasdnfbmwqera"))
    self.assertFalse(ts.palinperm("tact Coa dbo"))
    pass

if __name__ == '__main__':
  unittest.main()
  #cProfile.run('unittest.main()')
