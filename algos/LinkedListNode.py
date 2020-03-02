#!/usr/bin/env python
import unittest
from pprint import pprint as pp

class LinkedListNode():
  next = None;
  s = ""

  def __init__(self, string):
    self.s = string

  def mk_list(self):
    """ Return a list of values in the linked list from the current node to the end. """
    l, n = list(), self
    l.append(self.s)
    while not n.next == None:
      l.append(n.next.s)
      n = n.next
    return l

  def display(self):
    """ Display values in linked-list nodes from this node until the end. Print self then use next to continue recursively. """
    print(f"node: {self.s}")
    if not self.next == None:
      self.next.display()

  def appendToTail(self, s):
    """ Given a string create a new tail node to the linked list referred to by this node. Follow next pointers linearly to find the end, then append. """
    end = LinkedListNode(s)
    n = self
    while not n.next == None:
      n = n.next
    n.next = end
    return end

  def remove_from_middle(self, s):
    """ Given a string, find the node in the current linked list.  """
    if self.next == None:
      return False # We are in fact at the end of the list so do nothing.
    self.s = self.next.s
    self.next = self.next.next
    return True

  def remove_dupes(self):
    """ Given an unsorted singly linked list remove any duplicate nodes. As a secondary: can it be done without any additional data structure. """
    st = set()
    n,head = self,self
    st.add(n.s)
    while not n.next == None:
      if n.next.s in st:
        n.next = n.next.next
      else:
        st.add(n.next.s)
        n = n.next
    return head

  def remove_kth(self, k):
    n, head, ct = self, self, 1
    while not n.next == None:
      ct += 1
      n = n.next
    runner = 0
    n = head # reinitialize node pointer
    while runner < ct - k - 1:
      n = n.next
      runner += 1
    n.next = n.next.next

    return head

  def remove_this(self):
    """ Given pointer to a node in the middle of linked list, remove the current node keeping the rest of the list intact. """
    if self.next == None:
      return False # In this case we are actually at the end of the list so do nothing.
    self.s = self.next.s
    self.next = self.next.next
    return True

  def partition(self, v):
    """ Given a linked list node and a value, partition the list such that nodes less than the value appear to the left of all nodes greater than or equal to the value.
        Values within the two partitions do not need to be sorted. """
    runner, head = self, self
    while not runner.next == None:
      if runner == head: # head node can safely stay in place, start from second node
        runner = runner.next
        continue
      if runner.next.s < v: # compare next to value
        tmp = runner.next # delicate surgery
        runner.next = runner.next.next
        tmp.next = head
        head = tmp
      else:
        runner = runner.next
    return head

  def valuefromLN(self):
    """ Treat this linked list node as an integer whose digits are represented in the nodes. Return the value of this integer. """
    n = self
    result, power = 0,0
    while not n == None:
      result += int(n.s) * (10 ** power)
      power += 1
      n = n.next
    return result

  def addTo(self, num):
    """ Treat this linked list node and the given node in num as integer whose digits are represented by the linked list. The ones columned is indicated by the head node. """
    thisval = self.valuefromLN()
    thatval = num.valuefromLN()
    return thisval + thatval

  def isPalin(self):
    """ Return whether the set of strings represented in the given linked list is a palindrome. """
    s = self.mk_list()
    n = self
    for i in range(len(s) // 2): # floor of half length
      if not s[i] == s[~i]: # use 2's complement to compare successive elements from head and tail
        return False
    return True


  def __is__(self, n):
    return self.s == n.s

  def isIntersection(self, node):
    """ Given a linked list node, check if this linked list intersects with the given ll.  If yes, return the intersecting node.  If not, return None. """
    i,j = self, node
    ict, jct = 0, 0
    while not i == None:
      ict += 1
      i = i.next
    while not j == None:
      jct += 1
      j = j.next
    if not i is j:
      return None
    diff = abs(ict-jct)
    if ict > jct:
      longer = self
      shorter = node
    else:
      longer = node
      shorter = self

    # advance runner on longer to match shorter 
    for _ in range(diff):
      longer = longer.next

    while longer != None and shorter != None:
      if longer is shorter:
        return longer
      else:
        longer = longer.next
        shorter = shorter.next
    return None

  def main():
    pass

if __name__ == '__main__':
  main()
