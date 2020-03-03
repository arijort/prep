#!/usr/bin/env python
import unittest
import heapq
import sys
from pprint import pprint

class Stack():
  """ Python implementation of a stack: push onto stack, pop from stack, peek into Stack.  Depends on private class StackNode. """
  def __init__(self):
    self.head = None
    self.minnode = None
    return

  def popmin(self):
    return self.minnode

  def findmin(self):
    runner = self.head
    while runner != None:
      if runner.data < self.min:
        self.minval = runner.data

  def pop(self):
    if self.head == None:
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
    n = self.head
    while not n == None:
      print(n.data)
      n = n.next

  def mklist(self):
    n = self.head
    l = []
    while not n == None:
      l.append(n.data)
      n = n.next
    return l

  def isEmpty(self):
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
    self.assertEqual(arr, [ 'c','b','a'])
    c = stk.peek()
    self.assertEqual(c, 'c')
    c = stk.pop()
    arr = stk.mklist()
    self.assertEqual(arr, ['b','a'])
    b = stk.pop()
    arr = stk.mklist()
    self.assertEqual(arr, ['a'])
    self.assertFalse(stk.isEmpty())

    istk = Stack()
    istk.push(100)
    istk.push(10)
    istk.push(50)
    istk.push(20)
    arr = istk.mklist()
    self.assertEqual(arr, [20,50,10,100])
    m = istk.popmin()
    self.assertEqual(m.data, 10)
    istk.push(-40)
    m = istk.popmin()
    self.assertEqual(m.data, -40)

if __name__ == '__main__':
  unittest.main()
