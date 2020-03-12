#!/usr/bin/env python
import unittest
import math
#from joblib import Memory
from memoized import memoized

class Solution():
  def __init__(self):
    self.primes = set({2,3}) # prime the pump with set keep a running set of known primes below the given integer
    #self.primes = [2,3] # prime the pump with array
  def factors(self,n):
    """ https://projecteuler.net/problem=3
    Given a large numher find the prime factors. """

    result = []
    for p in self.primes:
      if 0 == n%p:
        result.append(p)
    for i in range(max(self.primes) + 2, n // 2):
      if self.is_prime(i): # otherwise check for primality and prime the prime array
        if n%i == 0 : #and self.is_prime(i):
          result.append(i)
    return result

  @memoized
  def is_prime(self,n):
    """ Given an integer, check if it's prime. """
    for p in self.primes:
      if 0 == n%p:
        return False
    for i in range(max(self.primes)+2, int(math.sqrt(n)+1),2 ):
      if 0 == n%i:
        return False
    self.primes.add(n)
    if len(self.primes) % 1000 == 0:
      print(f"{n} is prime")
      print(f"prime list is {len(self.primes)} long")
    return True

class Test(unittest.TestCase):
  def test_factors(self):
    ts = Solution()
    l = ts.factors(13195)
    self.assertEqual(l, [5,7,13,29])
    l2 = ts.factors(131953)
    self.assertEqual(l2, [127, 1039])
    l3 = ts.factors(191979)
    self.assertEqual(l3, [3, 83, 257])
    l = ts.factors(600851475143)
    self.assertEqual(l, [5,7,13,29])
    pass

if __name__ == '__main__':
  unittest.main()
