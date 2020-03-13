#!/usr/bin/env python
import unittest

class Solution():
  """ https://leetcode.com/problems/container-with-most-water/
  Given a list of integers which represent hiehgts of bars,
  find the larger possible area occupied by water as if it filled the container bounded by the 2 bars. """
  def container(self, height):
    print(f"working list length {len(height)}")
    cts = 0
    if len(height) < 2:
      return -1
    maxleft, maxleftx, maxrightx, maxarea = 0,0,0,0
    for x, val in enumerate(height):
      print(f"trying left side {x} ({val}) ")
      if val < maxleft:
        continue
      for x1 in range(x+1, len(height)):
        thisarea = (x1 - x) * min(val, height[x1])
        cts += 1
        print(f"  checking area between {x} ({val}) and {x1} ({height[x1]}) this: {thisarea} max: {maxarea}")
        if thisarea > maxarea:
          maxarea = thisarea
          maxleft = val
          maxleftx = x
          maxrightx = x1
    print(f"finished with {cts} comparisons")
    return maxarea

  def container2(self,height):
    #print(f"working list length {len(height)} {height}")
    cts = 0
    if len(height) < 2:
      return -1
    left, right = 0, len(height) -1
    maxleft, maxleftx = 0, height[0]
    maxright, maxrightx = len(height) - 1, height[-1]
    maxarea = (maxright - maxleft) * min(maxleftx, maxrightx)

    while right > left:
      if height[right] > height[left]:
        left += 1
      else:
        right -= 1
      thisarea = (right - left) * min(height[right], height[left])

      cts += 1
      if thisarea > maxarea:
        maxarea = thisarea
        maxleft = height[left]
        maxright = height[right]
        maxleftx = left
        maxrightx = right
    #print(f"ending with maxarea {maxarea} comparisons {cts} maxleft {maxleft} maxright {maxright} maxleftx {maxleftx} maxrightx {maxrightx}")
    return maxarea


class Test(unittest.TestCase):
  def test_container(self):
    ts = Solution()
    t1= [1,8,6,2,5,4,8,3,7 ]
    #self.assertEqual(ts.container2(t1), 49)
    t2 = [76,155,15,188,180,154,84,34,187,142,22,5,27,183,111,128,50,58,2,112,179,2,100,111,115,76,134,120,118,103,31,146,58,198,134,38,104,170,25,92,112,199,49,140,135,160,20,185,171,23,98,150,177,198,61,92,26,147,164,144,51,196,42,109,194,177,100,99,99,125,143,12,76,192,152,11,152,124,197,123,147,95,73,124,45,86,168,24,34,133,120,85,81,163,146,75,92,198,126,191]
    #self.assertEqual(ts.container2(t2), 18048)
    t3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277]
    #self.assertEqual(ts.container2(t3), 19182)
    t4 = list(range(15000,0,-1))
    self.assertEqual(ts.container2(t4), 56250000)
if __name__ == '__main__':
  unittest.main()
