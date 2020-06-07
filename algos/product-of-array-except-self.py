#!/usr/bin/env python
import unittest

class Solution():
  def productExceptSelf(self, nums):
    """ https://leetcode.com/problems/product-of-array-except-self/
    Given an array of integers _nums_, return a same-sized array _output_ where each element in _output_ is the product of all integers in _nums_ except itself. 
  
    Example:
      Input:  [1,2,3,4]
      Output: [24,12,8,6]
  
      output[3] = 6 because other values in nums multiply to 6: 1 * 2 * 3
  
    Technique:
      Iterate over the array twice. First from left to right gathering the cumulative product of integers to the left of each element. Then from right to left, gathering the running product of integers
      to the right of each element. The result is two same-sized arrays. The result will be an item-wise product of those 2 arrays.
  
      Time Complexity: O(N) because we are iterating over the given array twice.
      Space Complexity: O(N) because we create 2 additional arrays of size equal to the input array.
    """
    left_products  = [1] * len(nums)
    right_products = [1] * len(nums)

    left_running = 1
    for idx, num in enumerate(nums):
      left_products[idx] = left_running
      left_running *= num

    right_running = 1
    right_p = len(nums) - 1
    while right_p >=0:
      right_products[right_p] = right_running
      right_running *= nums[right_p]
      right_p -= 1

    for i in range(len(left_products)):
      left_products[i] *= right_products[i]

    return left_products

class Test(unittest.TestCase):
  def test_foo(self):
    ts = Solution()

    self.assertEqual( ts.productExceptSelf([1,2,3,4]), [24,12,8,6])

if __name__ == '__main__':
  unittest.main()
