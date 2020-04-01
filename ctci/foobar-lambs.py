#!/usr/bin/env python 
import unittest
import math

""" Given an integer value of lambs, allocate them to henchman according to the following rules in the most generous and most stingy manner.
  Return the difference between in the number of henchman you can support between the most generous and the most stingy paths. 
      1. The most junior henchman (with the least seniority) gets exactly 1 LAMB.  (There will always be at least 1 henchman on a team.)
      2. A henchman will revolt if the person who ranks immediately above them gets more than double the number of LAMBs they do.
      3. A henchman will revolt if the amount of LAMBs given to their next two subordinates combined is more than the number of LAMBs they get.  (Note that the two most junior henchmen won't have two subordinates, so this rule doesn't apply to them.  The 2nd most junior henchman would require at least as many LAMBs as the most junior henchman.)
      4. You can always find more henchmen to pay - the Commander has plenty of employees.  If there are enough LAMBs left over such that another henchman could be added as the most senior
                  while obeying the other rules, you must always add and pay that henchman.

"""
def solution(total_lambs):
  # start by allocating 1 to the first henchman: rule 1
  generous_henchmen_list, stingy_henchmen_list = [1], [1]
  generous_path_number = find_generous_path(total_lambs -1 , generous_henchmen_list)
  stingy_path_number   = find_stingy_path(total_lambs -1 , stingy_henchmen_list)
  print(f"from total {total_lambs}")
  print(f"found generous len {len(generous_path_number)} {generous_path_number} sum {sum(generous_path_number)} remaining {total_lambs - sum(generous_path_number)}")
  print(f"found stingy   len {len(stingy_path_number)} {stingy_path_number} sum {sum(stingy_path_number)} remaining {total_lambs - sum(stingy_path_number)}")
  return len(stingy_path_number) - len(generous_path_number)

def find_generous_path(total_lambs, henchmen):
  if total_lambs == 0:
    return henchmen
  if len(henchmen) == 1:
    henchmen.append(2)
    return find_generous_path(total_lambs - 2, henchmen)
  print(f"following generous path with lambs {total_lambs} and henchmen {henchmen}")
  subordinate_lambs = henchmen[-1]
  lambs_for_this_henchman = 2 * subordinate_lambs # default policy: be most generous
  
  if total_lambs >= lambs_for_this_henchman:
    henchmen.append(lambs_for_this_henchman)
    return find_generous_path(total_lambs - lambs_for_this_henchman, henchmen)
  if total_lambs > henchmen[-1] + henchmen[-2]:
    henchmen.append(total_lambs)
  return henchmen

def find_stingy_path(total_lambs, henchmen):
  if total_lambs == 0:
    return henchmen
  #print(f"following stingy path with lambs {total_lambs} and henchmen {henchmen}")
  if len(henchmen) == 1: # starting condition
    henchmen.append(1)
    return find_stingy_path(total_lambs - 1, henchmen)
  lambs_for_this_henchman = henchmen[-1] + henchmen[-2] # stingiest policy default: only sum of most recent 2, i.e. Fibonacci
  if total_lambs < lambs_for_this_henchman:
    return henchmen # done
  #print(f"recursing on stingy path with {total_lambs - lambs_for_this_henchman}")
  henchmen.append(lambs_for_this_henchman)
  return find_stingy_path(total_lambs - lambs_for_this_henchman, henchmen)

class Test(unittest.TestCase):
  def test_lambs(self):
    expects = [ (10,1), (143,3), (142,2), (1,0), (2,0), (3,0), (4,1), (5,1), (7,1), (8,1), (9,1) ]
    for num,expect in expects:
      self.assertEqual(expect, solution(num))
    for n in range(11,40):
      print(f"n {n} result {solution(int(math.pow(2,n)))}")
    for n in range(1100,1120):
      print(f"n {n} result {solution(n)}")
    solution(100000000)
    pass

if __name__ == '__main__':
  unittest.main(verbosity=2)
