#!/usr/bin/env python

class Solution:
  def findMedianSortedArrays(self, nums1, nums2):
    """ Given 2 sorted lists find the median value among the values in both lists.
    https://leetcode.com/problems/median-of-two-sorted-arrays/ """
    result = 0.0
    print("working lists %s and %s" % (str(nums1), str(nums2)))
    if nums1 == []:
      return self.simplemedian(nums2)
    if nums2 == []:
      return self.simplemedian(nums1)

    #concatarr = nums1 + nums2
    #print("concat array is %s" % str(sorted(concatarr)))
    l1, l2 = len(nums1), len(nums2)
    total = l1 + l2
    if l1 == 1 or l2 == 1:
      return self.simplemedian(sorted(nums1 + nums2))
    nums1l, nums2l = 0, 0
    nums1r, nums2r = l1 - 1, l2 - 1
    
    while nums1l + nums2l < total/2 and nums1r > 0 and nums2r > 0 and nums1l < l1 - 1 and nums2l < l2 - 1:
      print("working indices 1l %d 2l %d andddd 1r %d 2r %d" % (nums1l,nums2l,nums1r,nums2r))
      if nums1[nums1l] < nums2[nums2l]:
        nums1l += 1
      else:
        nums2l += 1
      if nums1[nums1r] < nums2[nums2r]:
        nums2r -= 1
      else:
        nums1r -= 1
    print("final indices 1l %d 2l %d andddd 1r %d 2r %d" % (nums1l,nums2l,nums1r,nums2r))
    print("final values 1l %d 2l %d andddd 1r %d 2r %d" % (nums1[nums1l],nums2[nums2l],nums1[nums1r],nums2[nums2r]))
    if not nums1l == nums1r and not nums2l == nums2r:
      print("returning %f" % self.simplemedian(sorted( [ nums1[nums1l],nums2[nums2l],nums1[nums1r],nums2[nums2r] ])))
      return self.simplemedian(sorted( [ nums1[nums1l],nums2[nums2l],nums1[nums1r],nums2[nums2r] ]))
    if nums1l == nums1r:
      final1 = [ nums1[nums1l] ]
    else:
      final1 = [ nums1[nums1l], nums1[nums1r] ]
    if nums2l == nums2r:
      final2 = [ nums2[nums2l] ]
    else:
      final2 = [ nums2[nums2l], nums2[nums2r] ]
    final = sorted(final1 + final2)
    print("final arr %s " % str(final))
    return self.simplemedian(final)

  def simplemedian(self, arr):
    mid = len(arr) // 2
    return ( arr[mid] + arr[~mid] ) / 2
  

def main():
  s = Solution()
  nums1 = [4,5,6,7,8]
  nums2 = [4,15,26,47,9]
  print("t1 should be 7.5 found result %s " % s.findMedianSortedArrays(sorted(nums1), sorted(nums2)) )
  nums1 = range(20)
  nums2 = range(10,35)
  print("t2 should be 15.5 found result %s " % s.findMedianSortedArrays(sorted(nums1), sorted(nums2)) )
  nums1 = [1,3]
  nums2 = [2]
  print("t3 should be 2 found result %s " % s.findMedianSortedArrays(sorted(nums1), sorted(nums2)) )
  nums1 = [3]
  nums2 = [-2,-1]
  print("t4 should be -1 found result %s " % s.findMedianSortedArrays(sorted(nums1), sorted(nums2)) )
  nums1 = []
  nums2 = [2]
  print("t5 should be 2 found result %s " % s.findMedianSortedArrays(sorted(nums1), sorted(nums2)) )
  nums1 = [1,2]
  nums2 = [3,4]
  print("t6 should be 2.5 found result %s " % s.findMedianSortedArrays(sorted(nums1), sorted(nums2)) )
  nums1 = [2,2,2,2]
  nums2 = [2,2,2]
  print("t7 should be 2.0 found result %s " % s.findMedianSortedArrays(sorted(nums1), sorted(nums2)) )
  nums1 = [1]
  nums2 = [2,3,4]
  print("t8 should be 2.5 found result %s " % s.findMedianSortedArrays(sorted(nums1), sorted(nums2)) )
  nums1 = [1]
  nums2 = [2,3,4,5]
  print("t9 should be 3.0 found result %s " % s.findMedianSortedArrays(sorted(nums1), sorted(nums2)) )
  nums1 = [3,4,5]
  nums2 = [1,2]
  print("t10 should be 3.0 found result %s " % s.findMedianSortedArrays(sorted(nums1), sorted(nums2)) )
  nums1 = [1,3]
  nums2 = [2,4,5,6,7,8,9,10,11]
  print("t11 should be 6 found result %s " % s.findMedianSortedArrays(sorted(nums1), sorted(nums2)) )


if __name__ == '__main__':
  main()
