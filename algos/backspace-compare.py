#!/usr/bin/env python
import unittest

class Solution():
  """ Given 2 strings which may contain # character, treat the hash as a backspace and return whether the 2 strings match after applying the backspaces.
  https://leetcode.com/problems/backspace-string-compare/ """
  def backspaceCompare(self, S: str, T: str) -> bool:
    print(f"running with s {S} and t {T}")
    s_result, t_result = [], []
    for letter in S:
      if letter == '#' and len(s_result) > 0:
        s_result.pop()
      elif letter != '#':
        s_result.append( letter )
    for letter in T:
      if letter == '#' and len(t_result) > 0:
        t_result.pop()
      elif letter != '#':
        t_result.append( letter )

    res =  s_result == t_result
    print(f"returning {res} from s {s_result} and t {t_result}")
    return res

  def backspaceCompare_cp(self, S: str, T: str) -> bool:
      def filter(word):
        new = []
        for letter in word:
          if letter != "#":
            new.append(letter)
          else:
            if len(new) > 0:
              new.pop()
        return "".join(new)
      return filter(S) == filter(T)

class Test(unittest.TestCase):
  def test_backspace_compare(self):
    ts = Solution()

    trues = [ ("ab#c", "ad#c"), ( "ab", "ab"), ("ab##", "cd##"), ("a##c", "#a#c"), ("y#fo##f", "y#f#o##f") ]
    falses = [ ("a#c", "b"), ( "ab", "abc")  ]

    [ self.assertTrue( ts.backspaceCompare(s,t) ) for s,t in trues ]
    [ self.assertFalse( ts.backspaceCompare(s,t) ) for s,t in falses ]

if __name__ == '__main__':
  unittest.main()
