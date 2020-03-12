#!/usr/bin/env python
import unittest
import math

class Solution():
  def isPalindrome(self,n):
    if n < 0:
      return False
    if n == 0:
      return True
    most_sig = int(math.log(n,10))
    num_digits = most_sig +1
    while most_sig >= 1:
      power_of_ten = 10**most_sig
      most_sig_digit = n // power_of_ten
      least_sig_digit = n % 10
      if most_sig_digit != least_sig_digit:
        return False
      n -= most_sig_digit * power_of_ten
      n //= 10
      most_sig -= 2
    return True

class Test(unittest.TestCase):
  def test_isPalindrome(self):
    ts = Solution()

    palindromes = [ 121, 74743892484238794238871367813613267813263127688672136231876231631876317883249783248429834747, 1221, 0, 2222222, 2222222]
    non_palindromes = [ 1234, 7474389248423879423887136781361326781326312768, -1221, 10 ]

    [ self.assertTrue( ts.isPalindrome(i) ) for i in palindromes ]
    [ self.assertFalse( ts.isPalindrome(i) ) for i in non_palindromes ]

if __name__ == '__main__':
  unittest.main()
