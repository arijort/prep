#!/usr/bin/env python
import unittest

class Solution():

  def minimumBribes(self,q):
    result = 0
    print(f"checking list {q}")
    for idx, person in enumerate(q):
      if person - (idx+1) > 2:
        print("Too chaotic")
        return
      if idx < 1:
        continue
      minperson = min(idx,person-2)
      print(f"checking {person} iterating from {idx} down to {minperson}")

      for runner in range(idx,minperson,-1):
        print(f"checking person {person} against {q[runner]} ")
        if q[runner] > person:
          print(f"found person {q[runner]} in front of {person}") 
          result += 1
    print(result)
    return(result)

class Test(unittest.TestCase):
  def test_foo(self):
    ts = Solution()

    self.assertEqual( ts.minimumBribes( [1, 2, 5, 3, 7, 8, 6, 4]), 7)
    self.assertEqual( ts.minimumBribes( [2, 1, 5, 3, 4]), 3)

if __name__ == '__main__':
  unittest.main()
