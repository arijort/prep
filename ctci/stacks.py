#!/usr/bin/env python
import unittest
#from pprint import pprint

class ThreeStackArray():
  """ Implement 3 stacks in a single array. """
  def __init__(self):
    """ Use the slots mod 3 to represent the three stacks. I.e. the first stack's nodes will be in array slots 0, 3, 6 etc.
    The second in 1, 4, 7 etc and the third in 2, 5, 8 etc. """
    self.array = [None, None, None] # initialization of the three stacks
    self.head = [-3, -2, -1]
    self.numstacks = 3

  def pop(self, n):
    """ Basic interface for the 3 stack includes an integer indicating whether we want to pop from stack 1, 2 or 3. """
    if not n < self.numstacks and n >= 0:
      return None # bad n value
    if self.head[n] == -1:
      return None # stack is empty
    node = self.array[self.head[n]]
    self.head[n] -= self.numstacks
    return node

  def peek(self, n):
    return array[head[n]]

  def push(self, n, data):
    newslot = self.head[n] + self.numstacks
    self.grow_until(newslot)
    self.array[newslot] = data
    self.head[n] = newslot

  def grow_until(self, length):
    if len(self.array) >= length + 1:
      return
    adds = length - len(self.array) + 1
    for _ in range(adds):
      self.array.append(None)

  def is_empty(self,n):
    return self.head[n] < 0

  def mk_list(self, n):
    """ Return an array containing each item in the stack with the given integer value. """
    result = []
    #for i in range(self.head[n], 0, -3):
    for i in self.array[self.head[n]::-3]:
      result.append(i)
    return result

class Stack():
  """ Python implementation of a stack: push onto stack, pop from stack, peek into Stack.
    Depends on private class StackNode. """
  def __init__(self):
    self.head = None
    self.minnode = None

  def popmin(self):
    return self.minnode

  def findmin(self):
    runner = self.head
    while runner is not None:
      if runner.data < self.minnode:
        self.minval = runner.data

  def pop(self):
    if self.head is None:
      return None
    node = self.head
    self.head = self.head.next
    if node == self.minnode:
      self.findmin()
    return node

  def push(self, data):
    node = StackNode(data)
    node.next = self.head
    self.head = node
    if self.minnode is None:
      self.minnode = node
      return
    if node < self.minnode:
      self.minnode = node
    return

  def peek(self):
    return self.head.data

  def display(self):
    runner = self.head
    while not runner is None:
      print(runner.data)
      runner = runner.next

  def mklist(self):
    runner = self.head
    lst = []
    while runner is not None:
      lst.append(runner.data)
      runner = runner.next
    return lst

  def is_empty(self):
    return self.head == None

class StackNode():
  def __init__(self, data):
    self.data = data
    self.next = None
  def __lt__(self, node):
    if self.data < node.data:
      return True
    else:
      return False
  def __gt__(self, node):
    if self.data > node.data:
      return True
    else:
      return False

class Test(unittest.TestCase):
  def test_stacks(self):
    stk = Stack()
    stk.push("a")
    stk.push("b")
    stk.push("c")
    arr = stk.mklist()
    self.assertEqual(arr, ['c', 'b', 'a'])
    c = stk.peek()
    self.assertEqual(c, 'c')
    c = stk.pop()
    arr = stk.mklist()
    self.assertEqual(arr, ['b', 'a'])
    stk.pop()
    arr = stk.mklist()
    self.assertEqual(arr, ['a'])
    self.assertFalse(stk.is_empty())

    istk = Stack()
    istk.push(100)
    istk.push(10)
    istk.push(50)
    istk.push(20)
    arr = istk.mklist()
    self.assertEqual(arr, [20, 50, 10, 100])
    themin = istk.popmin()
    self.assertEqual(themin.data, 10)
    istk.push(-40)
    themin = istk.popmin()
    self.assertEqual(themin.data, -40)

  def test_three_stacks(self):
    stk3 = ThreeStackArray()
    stk3.push(0, "a")
    stk3.push(1, "foob")
    stk3.push(0, "b")
    stk3.push(1, "barm")
    stk3.push(0, "c")
    stk3.push(1, "quuz")
    self.assertTrue(stk3.is_empty(2))
    stk3.push(2, 99)
    stk3.push(2, 79)
    stk3.push(2, 44)
    arr = stk3.mk_list(0)
    self.assertEqual(arr, ['c', 'b', 'a'])
    self.assertFalse(stk3.is_empty(0))
    self.assertFalse(stk3.is_empty(1))

if __name__ == '__main__':
  unittest.main()
