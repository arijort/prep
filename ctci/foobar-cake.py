#!/usr/bin/env python2.7
import unittest

def solution(s):
  l = len(s)
  max_slices = 1
  for divisor in range(l, 0, -1): 
    if l % divisor != 0: # skip this divisor if we can't make equal sized slices
      continue
    size_slice = int(l / divisor)
    cake_segments = [ s[i:i+size_slice] for i in range(0,l,size_slice) ]
    if len(set(cake_segments)) == 1:
      max_slices = max(max_slices, divisor)
  return max_slices

class Test(unittest.TestCase):
  def test_foobar_cake(self):
    ts1 = solution("abcabcabcabc")
    self.assertEqual(ts1, 4)
    ts2 = solution("abccbaabccba")
    self.assertEqual(ts2, 2)
    ts3 = solution("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvw")
    self.assertEqual(ts3, 1)
    ts4 = solution("abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")
    self.assertEqual(ts4, 7)
    ts5 = solution("aaaa")
    self.assertEqual(ts5, 4)
    pass

if __name__ == '__main__':
  unittest.main(verbosity=2)
