#!/usr/bin/env python
import unittest
from collections import defaultdict

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        self.count = 1 
    def do_in_order(self):
        if self.left:
            self.left.do_in_order()
        print(f"val {self.val} count {self.count}")
        if self.right:
            self.right.do_in_order()
    def do_pre_order(self):
        print(f"val {self.val} count {self.count}")
        if self.left:
            self.left.do_pre_order()
        if self.right:
            self.right.do_pre_order()
    def do_post_order(self):
        if self.left:
            self.left.do_post_order()
        if self.right:
            self.right.do_post_order()
        print(f"val {self.val} count {self.count}")
            

class Solution:
    """ https://leetcode.com/problems/count-of-smaller-numbers-after-self/
    Given a list of integers, create na equal lenght list where each item shows a count of the number of smaller numbers to the right. """
    def __init__(self):
        self.root = None
        self.count = 0

    def do_traversals(self):
        print(f"in order")
        self.root.do_in_order()
    
    def inset(self, root, val):
        if root == None :
            return Node(val)
        print(f"root val {root.val}, val {val}, root.count {root.count}")
        root.count +=1
        if root.val >= val:
            print(f"root val ge val")
            if root.left :
                self.inset( root.left, val)
            else:
                root.left = Node(val)
        else:
            print(f"root val lt val")
            self.count += 1
            if root.left:
                self.count += root.left.count 
            if root.right:
                self.inset( root.right, val)
            else:
                root.right = Node(val)
        print(f" node {root.val} count {root.count}")
        print(f" self count {self.count}")
                
    def countSmaller(self, nums):
        if nums == []:
            return []
        if len(nums) == 1:
            return [0]
        
        output = [0]
        self.root = Node(nums[-1])
        
        for ele in nums[::-1][1:]:
            self.count = 0
            print(ele)
            self.inset( self.root, ele)
            output.append(self.count)
            # print( )
            
        return output[::-1]

  #def countSmaller_bad(self, nums):
  #  result = [int] * len(nums)
  #  num_counts = defaultdict(int)
  #  num_seen_set = set()
  #  for idx, n in enumerate(nums[::-1]):
  #    num_seen_set.add(n)
  #    num_counts[n] += 1
  #    smaller_than = [ i for i in num_seen_set if i < n ]
  #    count = sum( num_counts[smaller] for smaller in smaller_than )
  #    result[~idx] = count
  #  return result



class Test(unittest.TestCase):
  def test_foo(self):
    ts = Solution()

    input_list = [5,2,6,1]
    expected = [ 2,1,1,0 ]
    self.assertEqual(ts.countSmaller(input_list), expected)

    big_input = [5183,2271,3067,539,8939,2999,9264,737,3974,5846,-210,9278,5800,2675,6608,1133,-1,6018,9672,5179,9842,7424,-209,2988,2757,5984,1107,2644,-499,7234,7539,6525,347,5718,-742,1797,5292,976,8752,8297,1312,3385,5924,2882,6091,-282,2595,96,1906,8014,7667,5895,7283,7974,-167,7068,3946,6223,189,1589,2058,9277,-302,8157,8256,5261,8067,1071,9470,2682,8197,5632,753,3179,8187,9042,8167,4657,7080,7801,5627,7917,8085,928,-892,-427,3685,4676,2431,8064,8537,343,505,4352,2108,4399,66,2086,1922,9126,9460,393,443,5689,7595,850,8493,2866,732,3738,7933,3666,2370,5804,4045,7903,8009,5387,5542,7593,6862,1547,6934,-160,9693,4560,7429,9989,7232,-594,587,6476,9277,4471,5979,6268,2419,6706,-727,1927,7361,9684,5519,2703,1723,5181,3545,4290,9421,4288,1656,1541,9632,1448,-490,4747,5416,4139,-845,3834,3349,8594,7882,2279,7777,9369,9917,8167,6799,-612,5604,5787,2615,7033,5986,-322,8631,1793,-612,3528,206,419,1413,8585,5658,-981,1391,8088,7035,6259,-651,3118,9105,4531,2569,7576,7981,838,5715,1387,8506,331,7844,9187,6812,1221,6916,2361,5869,1002,5944,344,310,-981,3541,960,7667,8478,6610,9678,6511,3891,468,1347,115,3683,-982,5993,1875,69,4723,9949,3097,6822,1809,4672,3064,4587,2228,-580,6866,8977,9224,-261,4311,5304,1169,-511,7881,4252,3520,517,1714,6316,9399,8902,-376,4452,-414,1282,8399,1582,4933,7642,6671,1530,6175,2321,7191,9479,7211,6559,4040,6830,7416,602,6970,7978,4941,2225,7949,7398,6964,5912,1328,9818,8268,-999,4800,2510,6984,918,2181,9142,6036,5447,4337,9459,9070,-171,5017,7625,2807,6172,7139,-966,5374,4320,1266,6637,7043,-636,4346,7651,2102,3936,6906,4677,2505,1357,6219,2778,5193,5994,4155,1350,9806,2404,9970,8132,1054,5197,1421,4908,1185,6817,7034,239,8012,1740,7582,8098,8786,3703,2030,8422,3912,3300,8238,4293,898,7025,4871,1781,3688,9833,2108,6812,4171]
    expected = [ 2,1,1,0 ]
    ts.countSmaller(big_input)
    #self.assertEqual(ts.countSmaller(big_input), expected)
    ts.do_traversals()

    pass

if __name__ == '__main__':
  unittest.main(verbosity=2)
