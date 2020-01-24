#!/usr/bin/env python

import timeit

# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None
  def show(self):
    this = self
    while not this == None:
      print("digit %d" % (this.val))
      this = this.next
      

class Solution(object):
  def addTwoNumbers(self, l1, l2):
#    def valueFromLN(ln):
#      exp, v = 0, 0
#      while not ln == None:
#        v += ln.val * 10 ** exp
#        ln = ln.next
#        exp += 1
#      return v
    p = None
    for n in str(self.valueFromLN(l1) + self.valueFromLN(l2)):
      thisln = ListNode(int(n))
      thisln.next, p = p, thisln
      #print("working digit %s" % n)
    #print("returning p %s" % p)
    return p
 
  def valueFromLN(self,ln):
    exp, v = 0, 0
    while not ln == None:
      v += ln.val * 10 ** exp
      ln = ln.next
      exp += 1
    return v

def main():
  #print("starting")
  ln1_1 = ListNode(2)
  ln1_2 = ListNode(4)
  ln1_3 = ListNode(3)
  ln1_1.next = ln1_2
  ln1_2.next = ln1_3
  #print("checking ln1 %s %s %s" % (ln1_1, ln1_1.val, ln1_1.next))
  #print("checking ln1 %s " % ln1_1.show() )

  ln2_1 = ListNode(5)
  ln2_2 = ListNode(6)
  ln2_3 = ListNode(4)
  ln2_1.next = ln2_2
  ln2_2.next = ln2_3

  sol = Solution()
  p = sol.addTwoNumbers(ln1_1, ln2_1)
  print("checking result ")
  p.show()

if __name__ == '__main__':
  main()
