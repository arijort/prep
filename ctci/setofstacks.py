#!/usr/bin/env python
import unittest
from stacks import Stack

class SetofStacks():
  """ Implement a stack using a set of stacks which can grow to a fixed length.
  The standard stack interface should pertain: pop, push, peek and is_empty. """
  def __init__(self, size):
    """ Initialize the set using the given size as the maximum size for a substack. """
    self.maxsize = size
    self.pointer = -1 # used to indicate which stack is the current active one. 
#    st = Stack()
    self.arr = [] # hold array of stacks
#    self.arr.append(st)

  def pop(self):
    """ Pop from the set of stacks.  Check if the active stack becomes empty after the pop then decrement pointer. """
    if self.is_empty():
      return None
    st = self.arr[self.pointer]
    result = st.pop()
    if st.is_empty():
      self.arr[self.pointer] = None
      self.pointer -= 1
    return result

  def push(self, data):
    """ Push to the set of stacks.  First check is the active stack is full, if so create a new one then push to that one and increment pointer. """
    if self.is_empty():
      st = Stack()
      self.arr.append(st)
      self.pointer = 0
      st.push(data)

    else:
      st = self.arr[self.pointer]
      if st.depth >= self.maxsize:
        self.pointer += 1
        st = Stack()
        self.arr.append(st)
      st.push(data)

  def peek(self):
    return self.arr[self.pointer].peek()

  def is_empty(self):
    return self.pointer == -1

  def mklist(self):
    if self.is_empty():
      return [None]
    result = []
    for i in range(self.pointer, -1, -1):
      result = result + self.arr[i].mklist() # list concat
    return result

class Test(unittest.TestCase):
  def test_setofstacks(self):
    stk = SetofStacks(12)
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

    istk = SetofStacks(12)
    istk.push(100)
    istk.push(10)
    istk.push(50)
    istk.push(20)
    arr = istk.mklist()
    self.assertEqual(arr, [20, 50, 10, 100])
    istk.push(-40)

    [ istk.push(i) for i in range(100) ]
    istk.mklist()

    popped_nodes = [ istk.pop() for i in range(4) ]
    result_values = [ i.data for i in popped_nodes ]
    self.assertEqual(result_values, [99, 98, 97, 96])
    popped_nodes = [ istk.pop() for i in range(200) ]
    istk.mklist()


if __name__ == '__main__':
  unittest.main()
