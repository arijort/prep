#!/usr/bin/env python
import unittest
def solution(prices, buyIndicator, sellIndicator):
  positions = [0] * len(prices)
  do_match_signals(prices, buyIndicator, positions, 1)
  do_match_signals(prices, sellIndicator, positions, -1)
  return positions

def do_match_signals(prices, indicators, positions, direction):
  stop_point = len(prices) - len(indicators)
  for i, price in enumerate(prices):
    sig_match = -1
    print(f"checking idx {i} price {price}")
    print(f"stop point {stop_point}")
    if i >= stop_point:
      break
    px_runner = i
    signal_p = 0
    #print(f"will check prices {prices[i:i+len(indicators)+1]} to signals {indicators}")
    while px_runner < len(prices) and signal_p < len(indicators): # iterate over prices from here forward
      # find next px change
      change_runner = px_runner + 1 # look for next change
      while prices[px_runner] == prices[change_runner]:
        change_runner += 1
      if change_runner > len(prices):
        break
      # look for match at this price change porint
      print(f"  comparing px_runner {prices[px_runner]} to {prices[change_runner]} with at p {indicators[signal_p]} ")
      match = do_match_signal(prices[px_runner], prices[change_runner], indicators[signal_p] )
      print(f"  got match {match}")
      if match == 1: # price change matches signal so increment both px and indicator
        px_runner = change_runner
        signal_p += 1
        if signal_p == len(indicators): # matched last indicator in signal so we are done with this price
          print(f"matched signal: do position change")
          sig_match = change_runner
      elif match == 0: # px was unchanged so only increment price runner
        px_runner += 1
        continue
      else:
        sig_match = -1
        break
    if sig_match > 0 :
      print(f"adding pos px_runner {sig_match} direction {direction}")
      positions[sig_match] += direction
      print(prices)
      print(positions)
  print(positions)
  return positions

def do_match_signal(p1,p2,signal):
  """ Return 1 if the signal "matches" meaning price increase while signal is 1 or price decrease while signal is -1 """
  # return -1 if no match
  # return 0 if no price change
  if p1 == p2:
    return 0
  if p1 < p2 and signal == 1:
    return 1
  if p1 > p2 and signal == -1:
    return 1 
  return -1

class Test(unittest.TestCase):
  def test_foo(self):
#    ts = Solution()


    self.assertEqual(solution( [51,56,56,58,60,59,54,57,52,48], [1,1], [-1,-1,1]), [0,0,0,1,2,0,0,-1,0,0])
    #self.assertEqual(solution( [51,56,56,58], [1,1], [-1,-1,1]), [0,0,0,1])

if __name__ == '__main__':
  unittest.main()

