#!/usr/bin/env python
import unittest
from stacks import Stack
#from pprint import pprint

class QueueViaStack():
  """ Implementation of a Queue using 2 stacks as the backing data structure.
    Depends on private class QueueNode. """
  def __init__(self):
    self.arr = [Stack(), Stack()]
    self.putstack, self.getstack = 0, 1 # 2 stacks have initial identities: puts will be pushed onto stack 0; while get will be retrieved via pop from stack 1

  def transfer(self):
    """ Implement switching nodes from the putstack to the get stack. """
    while not self.arr[self.putstack].is_empty():
      self.arr[self.getstack].push( self.arr[self.putstack].pop().data )

  def get(self):
    """ Get from the queue at the head. """
    if self.arr[self.getstack].is_empty():
      self.transfer()
    return self.arr[self.getstack].pop().data

  def put(self, data):
    """ Put on the putstack. """
    self.arr[self.putstack].push(data)

  def peek(self):
    if self.arr[self.getstack].is_empty():
      self.transfer()
    return self.arr[self.getstack].peek()

  def display(self):
    print("Putstack: ")
    self.arr[self.putstack].display()
    print("Getstack: ")
    self.arr[self.getstack].display()

  def mklist(self):
    puts = self.arr[self.putstack].mklist()
    puts.reverse()
    return self.arr[self.getstack].mklist() + puts

  def is_empty(self):
    return self.arr[self.putstack].is_empty() and self.arr[self.getstack].is_empty()

class Test(unittest.TestCase):
  def test_qvs(self):
    que = QueueViaStack()
    que.put("a")
    que.put("b")
    que.put("c")
    arr = que.display()
    arr = que.mklist()
    self.assertEqual(arr, ['a', 'b', 'c'])
    a = que.peek()
    self.assertEqual(a, 'a')
    a = que.get()
    arr = que.mklist()
    self.assertEqual(arr, ['b', 'c'])
    que.get()
    arr = que.mklist()
    self.assertEqual(arr, ['c'])
    self.assertFalse(que.is_empty())

    ique = QueueViaStack()
    ique.put(100)
    ique.put(10)
    ique.put(50)
    ique.put(20)
    g1 = ique.get()
    self.assertEqual(g1, 100)
    g2 = ique.get()
    self.assertEqual(g2, 10)
    g3 = ique.get()
    self.assertEqual(g3, 50)
    g4 = ique.get()
    self.assertEqual(g4, 20)
    ique.put(-40)

if __name__ == '__main__':
  unittest.main()
