#!/usr/bin/env python
import unittest
import collections 

class Solution(object):
  def sequenceReconstruction2(self, org, seqs):
    index = {num: i for i, num in enumerate([None] + org)}
    pairs = set(zip([None] + org, org))
    print(f"made index {index} and pairs{pairs}")
    for seq in seqs:
      print(f"  working seq {seq}")
      for a, b in zip([None] + seq, seq):
        print(f"    made a b {a} {b}")
        if index[a] >= index.get(b, 0):
          print(f"    return false early because index[a] {index[a]} index {index}")
          return False
        pairs.discard((a, b))
        print(f"    pairs after discard {pairs}")
    print(f"after sequences pairs {pairs}")
    return not pairs

  def sequenceReconstruction(self, org, seqs):
    """
    :type org: List[int]
    :type seqs: List[List[int]]
    :rtype: bool
    from https://leetcode.com/aayuskh
    """
    graph = {}
    inDegree = {}
    sources = collections.deque()
    sortedList = []
        
    # initialize graph & inDegree
    for seq in seqs:
      for num in seq:
        graph[num] = []
        inDegree[num] = 0
        
    # complete graph & fill inDegree
    # seq = [1,2,3] that means 1 = [2] & 2 = [3]
    for seq in seqs:
      for i in range(1, len(seq)):
        graph[seq[i-1]].append(seq[i])
        inDegree[seq[i]] += 1
    print(f"made graph to {graph} and inDegree {inDegree}")        
        
    # check if number of integers equals original integers
    if len(graph) != len(org):
      print(f"returning false early based on length comparison of graph {len(graph)} to orig {len(org)}")
      return False
        
    for num, count in inDegree.items():
      if count == 0:
        sources.append(num)
    print(f"created sources {sources}")

    while sources:
            
      # if anytime sources becomes equal or more than 2 that means many possiblity
      if len(sources) > 1:
        print(f"returning false early because len(sources) > 1 {len(sources)}")
        return False
            
      # this will keep check order of numbers in orginal
      print(f"orig snippet {org[len(sortedList)]} and sources {sources}") 
      if org[len(sortedList)] != sources[0]:
        return False
            
      num = sources.popleft()
      sortedList.append(num)
      print(f"made sorted list {sortedList}")
            
      for child in graph[num]:
        inDegree[child] -= 1
        if inDegree[child] == 0:
          print(f"appending child {child}")
          sources.append(child)
    return len(sortedList) == len(org)

class Test(unittest.TestCase):
  def test_foo(self):
    ts = Solution()

    trues = [ ( [1,2,3], [[1,2],[1,3],[2,3]] ) ,( [4,1,5,2,6,3], [[5,2,6,3],[4,1,5,2]] ) ]
    trues.append( ([4,1,5,2,6,3], [[5,2,6,3],[4,1,5,2], [4,1]] ) )
    #trues.append( ([4,1,5,2,6,3], [[2,6,3],[4,1,5], [4,1]] ) )
    falses = [ ([1,2,3], [[1,2],[1,3]] ), ( [1,2,3], [[1,2]]), ( [1,2,3], [[7,5], [9,8]]) ]
    falses.append( ([4,1,5,2,6,3], [[5,2,6,3], [4,1]] ) )

    [ self.assertTrue( ts.sequenceReconstruction(orig, seqs) ) for orig, seqs in trues ]
    [ self.assertFalse( ts.sequenceReconstruction(orig, seqs) ) for orig, seqs in falses ]
    [ self.assertTrue( ts.sequenceReconstruction2(orig, seqs) ) for orig, seqs in trues ]
    [ self.assertFalse( ts.sequenceReconstruction2(orig, seqs) ) for orig, seqs in falses ]

if __name__ == '__main__':
  unittest.main()
