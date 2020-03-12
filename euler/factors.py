#!/usr/bin/env python
import unittest
import math
#from joblib import Memory
from memoized import memoized
from functools import reduce
import sys

class Solution():
  def __init__(self):
    self.primes = set({2,3,5}) # prime the pump with set keep a running set of known primes below the given integer
    self.increment = 0
    #self.primes = [2,3] # prime the pump with array
  def get_next_prime(self):
    """ Given the current set of primes find the next one.
    Create a loop that only checks prime candidates 6k-1 (e.g. 5 11 17 23 29 35) and 6k+1 (e.g. 7 13 19 25)
    increments will alternate between 2 (5->7) and 4 (7->11) """
    increments = [2,4]
    n = max(self.primes) # this start with 5 at the beginning of the generator loop
    while n < 1_000_000:
      n += increments[self.increment]
      self.increment = ~ self.increment
      compo = False
      for p in self.primes:
        if n%p == 0:
          compo = True
          break # can stop iterating through primes because this candidate
      if compo:
        continue
      self.primes.add(n)
      yield n
    pass # should only reach here if we really run into the max integer

  def factors(self,n):
    """ https://projecteuler.net/problem=3
    Given a large number find the prime factors. """
    result = []
    i,ctp, ctc = 0,0,0
    for p in self.primes:
      ctp += 1
      if 0 == n%p:
        result.append(p)
        print(f"for {n} adding factor {p} after {ctp} prime compares in prime list {len(self.primes)}")
    while i < n // 2:
      i = next(self.get_next_prime())
      ctc += 1
      if n%i == 0: # is is assumed to be prime at this point
        result.append(i)
        print(f"for {n} adding factor {p} after {ctp} prime compares and {ctc} compares after prime list {len(self.primes)}")
        product = reduce((lambda x,y: x*y), result)
        if product == n:
          return result
    return result

class Test(unittest.TestCase):
  def test_factors(self):
    ts = Solution()
    l = ts.factors(13195)
    self.assertEqual(l, [5,7,13,29])
    l2 = ts.factors(131953)
    self.assertEqual(l2, [127, 1039])
    l3 = ts.factors(191979)
    self.assertEqual(l3, [3, 83, 257])
    l4 = ts.factors(491979)
    self.assertEqual(l4, [3, 163993])
    l5 = ts.factors(1491979)
    self.assertEqual(l5, [3, 163993])
    #l = ts.factors(600851475143)
    #self.assertEqual(l, [5,7,13,29])
    pass

if __name__ == '__main__':
  unittest.main()
