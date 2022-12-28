#!/usr/bin/env python
import unittest
import sys

class Solution():
  """ https://leetcode.com/problems/3sum-closest/description/ """
  # Given an array of integers and a target, find the set of 3 integers that comes closest to the target.
  # assume there is a single answer.

  def threeSumClosest(self, nums, target = 0):
    nums.sort()
    result = sys.maxsize
    for n,v in enumerate(nums):
      if n > 0 and v == nums[n-1]:
        continue
      # search in remaining space for a pair aiming for target
      seeking = target - v
      leftp,rightp = n + 1, len(nums)-1
      while leftp < rightp:
        testing = nums[leftp] + nums[rightp]
        if testing == seeking:
          result = v + testing
          break
        if abs(testing - seeking) < abs(target - result):
          result = v + testing
        elif testing > seeking:
          rightp -= 1
        else:
          leftp += 1
    return result

class Test(unittest.TestCase):
  def test_3sumcloset(self):
    ts = Solution()
    t1 = ts.threeSumClosest([-1, 2, 1, -4], 1)
    print("test 1 should be 2 %s" % t1)
    self.assertEqual(t1, 2)
    t2 = ts.threeSumClosest([0, 0, 0], 1)
    print("test 2 should solutions 0 %s" % t2)
    self.assertEqual(t2, 0)
if __name__ == '__main__':
  unittest.main()
