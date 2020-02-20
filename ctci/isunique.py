#!/usr/bin/env python
import unittest

def isunique(s):
  """ Function to determine whether a given string has unique values. """
  # 1 use a set to keep track, iterate
  st = set()
  for c in s:
    if c in st:
      return False
    else:
      st.add(c)

  return True

class UniqueTest(unittest.TestCase):
  """ Test whether a given string contains unique values.  No assumptions about sortedness of the string.
  https://github.com/careercup/CtCI-6th-Edition-Python/tree/master/Chapter1 """
  def test_unique(self):
    s1 = 'asdfg'
    self.assertTrue(isunique(s1))
    s2 = 'asdfiouasdfjkasdfg'
    self.assertFalse(isunique(s2))
    s3 = ''
    self.assertTrue(isunique(s3))

if __name__ == '__main__':
  unittest.main()
