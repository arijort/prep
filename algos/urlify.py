#!/usr/bin/env python
import unittest

class Solution():
  def urlify(self, s, l):
    """ Given a string and , make it suitable for adding to a URL by replacing spaces with '%20' """ 
    result = list()
    print(f"string is {s} length {l}")
    for _, c in enumerate(s):
      if c == " ":
        result.append("%20")
      else:
        result.append(c)
    res_str = "".join(result)
    return res_str

class Test(unittest.TestCase):
  def test_urlify(self):
    ts = Solution()
    self.assertEqual(ts.urlify("this is a string", 22), "this%20is%20a%20string")
    self.assertEqual(ts.urlify("", 0), "")
    pass

if __name__ == '__main__':
  unittest.main()
