#!/usr/bin/env python
import unittest

class Solution():
  """ https://leetcode.com/problems/non-decreasing-array/
  Given an array, check whether it can be made in to a non-decreasing array with at most one change.

  Technique: Iterate over array.
  At each step, track the maximum value.
  if the 
  """
  def checkPossibility(self, nums) -> bool:

    num_strikes = 0

    #print(f"checking list {nums} len {len(nums)}")
    for n in range(1, len(nums)):
      #print(f"comparing n {nums[n]} with n-1 {nums[n-1]}")
      if nums[n] < nums[n-1]:
      #  print(f"  adding one strike ")
        num_strikes += 1
    #print(f"result { num_strikes < 2}")
    return num_strikes < 2

class Test(unittest.TestCase):
  def test_foo(self):
    ts = Solution()

    trues = [ [1,2,3,4] , [ 2,1,4 ], [4,2,3 ] ]
    falses = [ [ 4,3,2], [4,2,1], [3,4,2,3] ]

    [ self.assertTrue( ts.checkPossibility(i) ) for i in trues ]
    [ self.assertFalse( ts.checkPossibility(i) ) for i in falses ]
    self.assertTrue(True)
    pass

if __name__ == '__main__':
  unittest.main()
