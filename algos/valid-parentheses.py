#!/usr/bin/env python
import unittest

class Solution():
  def isValid(self, s: str) -> bool:
    if len(s) == 0: return True
    if len(s) == 1: return False
    stack = []
    opens  = { '(':1 , '[':2, '{':3 }
    closes = { ')':1 , ']':2, '}':3 }
    for ch in s:
      if ch in opens:
        stack.append(ch)
      elif ch in closes:
        if not stack or closes[ch] != opens[stack[-1]]:
          return False
        stack.pop()
    return not stack

class Test(unittest.TestCase):
  def test_foo(self):
    ts = Solution()
    self.assertTrue(ts.isValid("()") )
    self.assertTrue(ts.isValid("()[]{}") )
    self.assertTrue(ts.isValid("[()]{}") )
    self.assertTrue(ts.isValid("([]{})") )
    self.assertFalse(ts.isValid("(]") )
    self.assertFalse(ts.isValid("()[{}") )
    self.assertFalse(ts.isValid("([)]") )
    self.assertFalse(ts.isValid("(") )
    self.assertFalse(ts.isValid("]") )
    self.assertTrue(True)
    pass

if __name__ == '__main__':
  unittest.main()
