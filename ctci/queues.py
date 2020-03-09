#!/usr/bin/env python
import unittest
#from pprint import pprint

class Queue():
  """ Python implementation of a Queue: put onto queue at tail, get from queue at head, peek into Queue.
    Depends on private class QueueNode. """
  def __init__(self):
    self.head = None
    self.tail = None
    self.depth = 0

  def get(self):
    """ Get from the queue at the head. """
    if self.head is None:
      return None
    node = self.head
    self.head = self.head.next
    self.depth -= 1
    return node

  def put(self, data):
    """ Put on the tail of the queue. """
    node = QueueNode(data)
    if self.tail is not None:
      self.tail.next = node
    self.tail = node
    self.depth += 1
    if self.head is None:
      self.head = node
    return

  def peek(self):
    return self.head.data

  def display(self):
    runner = self.head
    while not runner is None:
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

class QueueNode():
  """ Implementation of a node in a queue. """
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
  def test_queues(self):
    que = Queue()
    que.put("a")
    que.put("b")
    que.put("c")
    arr = que.mklist()
    self.assertEqual(arr, ['a', 'b', 'c'])
    c = que.peek()
    self.assertEqual(c, 'a')
    c = que.get()
    arr = que.mklist()
    self.assertEqual(arr, ['b', 'c'])
    que.get()
    arr = que.mklist()
    self.assertEqual(arr, ['c'])
    self.assertFalse(que.is_empty())

    ique = Queue()
    ique.put(100)
    ique.put(10)
    ique.put(50)
    ique.put(20)
    arr = ique.mklist()
    self.assertEqual(arr, [100, 10, 50, 20])
    ique.put(-40)

if __name__ == '__main__':
  unittest.main()
