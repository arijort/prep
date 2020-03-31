#!/usr/bin/env python
import unittest

class Solution():
  """ https://www.interviewcake.com/question/python3/coin
  Given a set of denominations and an amount, produce the number of ways that amount can be made with those denominations. 
  """
  def coin_possibilities(self,amount,denominations):
    print(f"working {amount} with denom {denominations}")
    ways_to_do_n_amount = [0] * (amount + 1) 
    ways_to_do_n_amount[0] = 1

    for coin in denominations:
      print(f"  doing coin {coin}")
      for higher_amount in range(coin, amount + 1):
        higher_amount_remainder = higher_amount - coin
        print(f"    doing amount {amount} with higher amount {higher_amount} remainder {higher_amount_remainder}")
        print(f"    adding {ways_to_do_n_amount[higher_amount_remainder]}")
        ways_to_do_n_amount[higher_amount] += ways_to_do_n_amount[higher_amount_remainder]
        print(f"    ways_to_do_n_amount [ {higher_amount} ] is now {ways_to_do_n_amount[higher_amount]}")
    print(f"result for amount {amount} is {ways_to_do_n_amount[amount]} ")
    print(f"full list {ways_to_do_n_amount}")
    return ways_to_do_n_amount[amount]


class Test(unittest.TestCase):
  def test_foo(self):
    ts = Solution()

    self.assertEqual( ts.coin_possibilities(5, [1,3,5]), 3)

if __name__ == '__main__':
  unittest.main()
