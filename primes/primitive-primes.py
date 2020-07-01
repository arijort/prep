#!/usr/bin/env python
import unittest

def primprimes(prime):
  """
  https://www.hackerrank.com/challenges/primitive-problem/problem
  Given a prime number between 2 and 10^9, return the smallest "primitive root" of the prime and the number of primitive roots.
  """
  primroots = []
  for g in range(prime):
    gmods = set()
    for exp in range(prime - 1):
      testing = (g ** exp) % prime
      print(f"checking  {g}^{exp} mod {prime} = {testing}")
      if testing in gmods:
        print("  repeat")
        break
      else: 
        gmods.add(testing)
    else:
      print(f"adding g {g}")
      primroots.append(g)

  return str(primroots[0]) + " " + str(len(primroots))

class Test(unittest.TestCase):
  def test_foo(self):

    self.assertEqual( primprimes(7), "3 2" )
    self.assertEqual( primprimes(11), "3 2" )
    pass

if __name__ == '__main__':
  unittest.main()
