#!/usr/bin/env python
import unittest
import cProfile

class Solution():
  def oneaway(self, a, b):
    """ Given two strings and the set of three rules of string changes, return whether the 2 strings are one edit or zero edits away from each other.
    Three permissible edits are as follows: single leter inserts, deletions and replacements. """
    alen, blen = len(a), len(b)
    if alen == blen:
      return self.handle_same_length(a,b)
    # assumption: deletion of a longer char from a longer string is the opposite operation to an insert .
    # Therefore we categorize strings as longer and shorter we can reduce the number of operations to check down to 2.
    if alen == blen + 1:
      return self.handle_one_off(b, a)
    elif blen == alen + 1:
      return self.handle_one_off(a, b)
    return False

  def handle_one_off(self, shorter, longer):
    """ Handle one-away logic for the case when the 2 strings' length differs by one.  Expect the caller to pass the shorted string as 'shorter', the first arg. """
    found = False
    for n, c in enumerate(shorter):
      if shorter[n] == longer[n]:
        continue
      elif shorter[n] == longer[n+1]:
        if not found:
          found = True
      else:
        return False
    return True

  def handle_same_length(self, a, b):
    """ Handle one-away logic in the case when 2 strings are found to be the same length. """
    found = False
    for i, j in zip(a, b):
      if i == j:
        continue
      elif found:
        return False # this case is the second found edit, thus return false
      else:
        found = True
    return True

class Test(unittest.TestCase):
  def test_oneaway(self):
    ts = Solution()
    self.assertTrue(ts.oneaway("pale", "pale"))
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
