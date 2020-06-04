#!/usr/bin/env python
import unittest


class Solution():
  """ https://leetcode.com/problems/reverse-vowels-of-a-string/
  Given a string, return a string with the vowels reversed. 

  Technique: create a list of chars representing the string. Note the original string is immutable.
  Use a left and right pointer to increment through the array seeking vowels only. When the left and right pointers are on vowels, we swap them, then move on.

  Time Complexity: O(N) because we iterate over the entire length of the string once.
  Space Complexity: O(N) because we create one copy of the entire string.
  """
  def reverseVowels(self, s):
    result = list(s)
    vowel_set = set( [ 'a', 'e', 'i', 'o', 'u'] )
    leftidx , rightidx = 0, len(s) - 1
    while leftidx < rightidx:
      while not s[leftidx] in vowel_set:
        leftidx += 1
      while not s[rightidx] in vowel_set:
        rightidx -= 1
      result[leftidx], result[rightidx] = s[rightidx], s[leftidx]
      leftidx += 1
      rightidx -= 1
    return "".join(result)


class Test(unittest.TestCase):
  def test_foo(self):
    ts = Solution()

    self.assertTrue(True)
    self.assertEqual( ts.reverseVowels("hello"), "holle")
    self.assertEqual( ts.reverseVowels("leetcode"), "leotcede")

if __name__ == '__main__':
  unittest.main()
