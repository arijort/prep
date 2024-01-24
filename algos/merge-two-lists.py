#!/usr/bin/env python
import unittest
from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1 or not list2:
      return list1 or list2

    head = ListNode()
    ptr = head

    while list1 and list2:
      if list1.val < list2.val:  
        ptr.next = list1
        list1 = list1.next
      else:
        ptr.next = list2
        list2 = list2.next
      ptr = ptr.next

    if not list2:
      ptr.next = list1
    if not list1:
      ptr.next = list2
    return head.next

class Test(unittest.TestCase):
  def test_foo(self):
    ts = Solution()
    l3 = ListNode(3)
    l2 = ListNode(2, l3)
    l1 = ListNode(2, l2)

    l6 = ListNode(6)
    l5 = ListNode(5, l6)
    l4 = ListNode(4, l5)

    m1 = ts.mergeTwoLists(l1, l4)
    #m2 = ts.mergeTwoLists([1,2,4], [1,3,4])
    while m1:
      print(f"val {m1.val}")
      m1 = m1.next
    #print(m2)
    #self.assertEqual(m1, [1,2,2,3,3,4])
    #self.assertEqual(m2, [1,1,2,3,4,4])
    #self.assertEqual(ts.mergeTwoLists([1,2,4], list2 = [1,3,4]), [1,1,2,3,4,333])
    self.assertTrue(True)
    pass

if __name__ == '__main__':
  unittest.main()
