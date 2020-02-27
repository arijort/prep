#!/usr/bin/env python
import unittest

class Solution():
  def string_rotation(self, s1, s2):
    """ Given a pair of strings return whether one string is a rotation of the other.  Aim to make one and only 1 call to a given function isSubstring. """
    # check if s1 is a substring of a concatenation of s2 doubled up.
    if not len(s1) == len(s2):
      return False
    return self.isSubstring(s2 + s2, s1)

  def isSubstring(self, string, substring):
    """ Given a pair of strings return whether the second string is a substring of the first. """
    print(f"searching {substring} in {string}")
    # idiomatic python:
    # return not string.find(substring) == -1
    for i in range(len(string) - len(substring)):
      teststr = string[i:i+len(substring)]
      print(f"checking {substring} against {teststr} in {string}")
      if teststr == substring:
        return True
    return False

class Test(unittest.TestCase):
  def test_string_rotation(self):
    ts = Solution()
    s1 = "waterbottle"
    s2 = "erbottlewat"
    self.assertTrue(ts.string_rotation(s1, s2))
    s1 = "lewaterb"
    s2 = "erbottlewat"
    self.assertFalse(ts.string_rotation(s1, s2))
    s1 = "asdlewaterb"
    s2 = "erbottlewat"
    self.assertFalse(ts.string_rotation(s1, s2))
    s1 = "lewaterbott"
    s2 = "erbottlewat"
    self.assertTrue(ts.string_rotation(s1, s2))
    pass

if __name__ == '__main__':
  unittest.main()
