#!/usr/bin/env python
import unittest
from collections import defaultdict

class Solution():
  """ https://leetcode.com/problems/bulls-and-cows/
  Given a secret string and a guess at that string, return a hint indicating how many characters are correct in value and position (bulls),
  and how many are correct in value only (cows).
  Bulls are indicated with 'A', cows with 'B' """
  def bulls_and_cows(self, secret, guess):
    bull_ct, cow_ct = 0, 0
    secret_d,extra_guesses = defaultdict(int), []
    for i, c in enumerate(guess):
      if secret[i] == c:
        bull_ct += 1
      else:
        secret_d[secret[i]] += 1
        extra_guesses.append(c)

    for char in extra_guesses:
      if secret_d[char] > 0:
        secret_d[char] -= 1
        cow_ct += 1

    return str(bull_ct) + "A" + str(cow_ct) + "B"


class Test(unittest.TestCase):
  def test_bulls_and_cows(self):
    ts = Solution()

    self.assertEqual( ts.bulls_and_cows("1807", "7810"), "1A3B" )
    self.assertEqual( ts.bulls_and_cows("1123", "0111"), "1A1B" )
    self.assertEqual( ts.bulls_and_cows("1122", "2211"), "0A4B" )
    self.assertTrue(True)
    pass

if __name__ == '__main__':
  unittest.main()
