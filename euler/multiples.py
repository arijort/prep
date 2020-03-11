#!/usr/bin/env python
import unittest
import collections
from collections.abc import Hashable
import functools

class memoized(object):
   '''Decorator. Caches a function's return value each time it is called.
   If called later with the same arguments, the cached value is returned
   (not reevaluated).
   '''
   def __init__(self, func):
      self.func = func
      self.cache = {}
   def __call__(self, *args):
      if not isinstance(args, Hashable):
         # uncacheable. a list, for instance.
         # better to not cache than blow up.
         return self.func(*args)
      if args in self.cache:
         return self.cache[args]
      else:
         value = self.func(*args)
         self.cache[args] = value
         return value
   def __repr__(self):
      '''Return the function's docstring.'''
      return self.func.__doc__
   def __get__(self, obj, objtype):
      '''Support instance methods.'''
      return functools.partial(self.__call__, obj)


class Solution():
  """ https://projecteuler.net/problem=2
  By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms. """

  @memoized
  def nth_fibonacci(self,n):
    """ Find the nth fibonacci number in the sequence. """
    #print(f"checking fibonacci sequence n={n}")
    if n < 0:
      return 0
    if n == 0 or n == 1:
      return n
    else:
      return self.nth_fibonacci(n-1) + self.nth_fibonacci(n-2)

  def show_fibs_until(self,n):
    """ Given a positive integer, return a list of numbers in the fibonacci sequence less than the number. """
    result = []
    if n < 1:
      return result
    arr = [0,1]
    for i in range(2,n):
      nextval = arr[i-1] + arr[i-2]
      if nextval > n:
        return arr
      else:
        arr.append( arr[i-1] + arr[i-2] )



class Test(unittest.TestCase):
  def test_fibs(self):
    ts = Solution()
    s = ts.nth_fibonacci(25)
    self.assertEqual(75025,s)

    l = ts.show_fibs_until(4_000_000)
    s = sum([ i for i in l if 0 == i%2])
    self.assertEqual(4613732,s)
    print(f"sum is {s}")

if __name__ == '__main__':
  unittest.main()

