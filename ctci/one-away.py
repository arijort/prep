#!/usr/bin/env python
import unittest
import cProfile

class Solution():
  def oneaway(self, a, b):
    """ Given two strings and the set of three rules of string changes, return whether the 2 strings are one edit or zero edits away from each other.
    Three permissible edits are as follows: single leter inserts, deletions and replacements. """
    if a == b:
      return True # handle zero edit check
    alen, blen = len(a), len(b)
    if abs(alen - blen) > 1:
      return False # handle cse where string length difference implies more than 1 edit/delete
    found, samelength = False, False
    if alen == blen:
      samelength = True
    # assumption: deletion of a longer char from a longer string is the opposite operation to an insert .
    # Therefor is we categorize strings as longer and shorte we can reduce the number of operations to check down to 2.
    if alen > blen:
      shorter, longer = b, a
    else:
      shorter, longer = a, b
    
    for n, c in enumerate(shorter):
      if shorter[n] == longer[n]:
        continue
      elif samelength:
        if found:
          return False
        else:
          found = True
          continue
      elif shorter[n] == longer[n+1]:
        if not found:
          found = True
      else:
        return False
    return True

class Test(unittest.TestCase):
  def test_oneaway(self):
    ts = Solution()
    self.assertTrue(ts.oneaway("pale", "ple"))
    self.assertTrue(ts.oneaway("pales", "pale"))
    self.assertTrue(ts.oneaway("pale", "bale"))
    self.assertFalse(ts.oneaway("pale", "bake"))
    self.assertFalse(ts.oneaway("pale", "ble"))
    self.assertTrue(ts.oneaway("paleabc", "pleabc"))
    self.assertTrue(ts.oneaway("", "d"))
    self.assertTrue(ts.oneaway("d", "de"))
    self.assertTrue(ts.oneaway("ple", "pale"))
    self.assertFalse(ts.oneaway("pale", "pse"))
    self.assertTrue(ts.oneaway("ples", "pales"))
    self.assertFalse(ts.oneaway("pas", "pale"))
    self.assertTrue(ts.oneaway("pale", "pkle"))
    self.assertFalse(ts.oneaway("pkle", "pable"))
    self.assertFalse(ts.oneaway("pal", "palks"))
    self.assertFalse(ts.oneaway("palks", "pal"))

if __name__ == '__main__':
  unittest.main()
  #cProfile.run('unittest.main()')
