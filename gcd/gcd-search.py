#!/usr/bin/env python
import unittest

def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)

def gcdsearch(numlist):
  """
  https://www.hackerrank.com/challenges/sherlock-and-gcd/problem
  Sherlock is stuck while solving a problem: Given an array A of integers he wants to know if there exists a subset B of this array which follows these statements:

     B is a non-empty subset.  There exists no integer > 1 which divides all elements of .
     There are no elements of B which are equal to another.
  Return a boolean indicating if a subset B exists.
  """
  numset = set()
  numset.add( numlist[0] )
  for n in numlist:
    if n == 1: # short circuit always, we can always return true with a subset of 1
      return True
    newgcd = gcd(numset.pop(),n)
    if newgcd == 1:
      return True
    else:
      numset.add(newgcd)
  return False

class Solution():
  def foo(self):
    pass

class Test(unittest.TestCase):
  def test_foo(self):
    ts = Solution()

    trues = [ [1,2,3], [3, 4,5] ]
    falses = [ [5, 5, 5], [2,4] ]

    [ self.assertTrue( gcdsearch(i) ) for i in trues ]
    [ self.assertFalse( gcdsearch(i) ) for i in falses ]
    self.assertTrue(True)
    pass

if __name__ == '__main__':
  #trues = [ [1,2,3], [3, 4,5] ]
  #falses = [ "555", "24" ]
  #nums  = [ alist for alist in trues ]
  #print(f"nums is {nums}")

  unittest.main()
