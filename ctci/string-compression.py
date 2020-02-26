#!/usr/bin/env python
import unittest

class Solution():
  def string_compression(self, s):
    """ Given a string, implement a basic compression algorithm in which each sequence of repeated characters is replaced with the character and an integer
    representing the number consecutive instances of that character.  E.g. aabcccccaaa would be replaced with a2b1c5a3. """
    result = list()
    currentchar = ""
    currentct = 0
    for n, c in enumerate(s):
      if not currentchar == c:
        if not currentchar == "":
          result.append(str(currentct))
          currentct = 0
        currentchar = c
        result.append(c)
      currentct += 1
    result.append(str(currentct))
    if len(result) > len(s):
      return s
    else:
      return "".join(result)

class Test(unittest.TestCase):
  def test_string_compression(self):
    ts = Solution()
    self.assertEqual(ts.string_compression("aabcccccaaa"), "a2b1c5a3")
    self.assertEqual(ts.string_compression("abc"), "abc")
    pass

if __name__ == '__main__':
  unittest.main()
