#!/usr/bin/env python
import unittest
import sys

class SetWithHistoryHashOnSequence():
  """ Implement a set with history using a backing hash table with the sequence number as the keys. """
  """ This implementation has irredeemable flaws. Assignment to current_set in add and discard does not copy the set by value. It copies by reference. """
  def __init__(self):
    self.latest_time = 0
    self.current_set = set()
    self.timestamps = { self.latest_time: self.current_set }

  def add(self, member):
    current_set = self.timestamps[self.latest_time]
    self.latest_time += 1
    current_set.add(member)
    self.timestamps[self.latest_time] = current_set
    return self.latest_time
  def discard(self, member):
    current_set = self.timestamps[self.latest_time]
    self.latest_time += 1
    current_set.discard(member)
    self.timestamps[self.latest_time] = current_set
    return self.latest_time
  def members_at(self, seq):
    print(self.timestamps)
    return self.timestamps[self.latest_time]

class Solution():
  """ Requirements delivered verbally.
  Implement a set with history.  This done nu implementing 3 methods:
    add() will take a member to be added to the set and return a value indicating the set contains this member as of this sequence point.
    discard() will take a member to be removed from the set and return a value indicating the set no longer contains this member as of this sequence point.
  """
  def __init__(self):
    # Use hash table to represent each member
    # member hash: { a: (1,3), b: (2,inf) }
    self.members = {}
    self.seq = 0 # Initial sequence value of 0 to indicate that set is empty at start time.

  def add(self, member):
    """ Add the given member to the set. Return the new sequence number indicating the add has been completed.
    Future calls to members() with the returned sequence value should include this member. """
    self.seq += 1
    if not member in self.members:
      self.members[member] = (self.seq, sys.maxsize)
    return self.seq

  def discard(self, member):
    """ Remove the given member from the set and return the sequence number indicating the member is no longer a member of the set as of that sequence point. """
    self.seq += 1
    if member in self.members:
      initial = self.members[member][0]
      self.members[member] = (initial, self.seq)
    return self.seq

  def members_at(self, seq):
    """ members(seq) will take a given sequence number and return the members that were present in the set as of that sequence point. """
    result = set()
    for m in self.members:
      start = self.members[m][0]
      if seq >= start and seq < self.members[m][1]:
        result.add(m)
    print(self.members)
    return result

class Test(unittest.TestCase):
  def test_foo(self):
    ts = Solution()

    seq1 = ts.add("a")
    seq2 = ts.add("b")
    first_set = ts.members_at(seq2)
    seq3 = ts.discard("a")
    ts.add("c")
    ts.add("d")
    ts.add("e")
    second_set = ts.members_at(seq3)

    self.assertEqual(sorted(first_set), ["a", "b"])
    self.assertEqual(sorted(second_set), ["b"])

    swh = SetWithHistoryHashOnSequence()
    seq1 = swh.add("aa")
    seq2 = swh.add("bb")
    first_set = swh.members_at(seq2)
    self.assertEqual(sorted(first_set), ["aa", "bb"])
    seq3 = swh.discard("aa")
    second_set = swh.members_at(seq3)
    self.assertEqual(sorted(second_set), ["bb"])
    seq2 = swh.add("cc")
    seq2 = swh.add("dd")
    seq2 = swh.add("ee")
    second_set = swh.members_at(seq3)

if __name__ == '__main__':
  unittest.main()
