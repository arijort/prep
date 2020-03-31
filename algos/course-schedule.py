#!/usr/bin/env python
import unittest
from collections import defaultdict, deque

class Solution():
  """ https://leetcode.com/problems/course-schedule/
  Given a list of course pairs in the form [A,B] where B is a prerequisite for course A,
  return whether it's possible to complete all the course.
  In Other words if there is a cycle we should return false. """
  def canFinish(self, n, courses):
    if n == 1 or not courses: return True
    course_dict = defaultdict(list)
    for course, prereq in courses:
      course_dict[course].append(prereq)
    return True

  def can_finish_dfs(self, n, courses):
    self.graph = defaultdict(list)
    self.visiting = set()
    self.visited = set()
    def do_dfs(course):
      if course in self.visited:
        print(f"    doing course {course} found visited return false")
        return False
      if course in self.visiting:
        print(f"    doing course {course} found cycle")
        return True # found a cycle
      self.visiting.add(course)
      for prereq in self.graph[course]:
        if do_dfs(prereq):
          print(f"    doing course {course} returning false")
          return False
      self.visiting.remove(course)
      self.visited.add(course)

    for course, prereq in courses:
      self.graph[course].append(prereq)
    print(f"dfs made graph {self.graph}")
    for course in range(n):
      if do_dfs(course): # dfs found a cycle so return false
        print(f"  dfs found cycle on course {course}")
        return False
    return True

  def can_finish_topo_sort2(self, n, course_pairs):
    return len(self.can_finish_topo_sort_find_order(n,course_pairs)) > 0

  def can_finish_topo_sort_find_order(self, n, course_pairs):
    child =  defaultdict(set)
    parent = defaultdict(int)
    for course, prereq in course_pairs:
      child[prereq].add(course)
      parent[course] += 1

    q = deque()
    for i in range(n):
      if parent[i] == 0:
        del parent[i]
        q.append(i)
    if not q:
      return []
    res = []
    while q:
      course = q.popleft()
      res.append(course)
      for c in child[course]:
        parent[c] -= 1
        if parent[c] == 0:
          del parent[c]
          q.append(c)
    print(f" have result {res}")
    if len(res) == n:
      return res
    else:
      return []


  def can_finish_topo_sort(self, n, course_pairs):
    """ Use topological sort to derive whether we can complete course work. """
    graph = defaultdict(GNode)
    total_deps = 0
    for course, prereq in course_pairs:
      graph[prereq].out_nodes.append(course)
      graph[course].in_degrees += 1
      total_deps += 1

    print(f"made graph {graph.keys()}")
    
    no_dep_courses = deque()
    for index, node in graph.items():
      print(f"  have index {index} node {node} in_degree {node.in_degrees} outnodes {node.out_nodes} ")
      if node.in_degrees == 0:
        no_dep_courses.append(index)

    removed_edges = 0
    while no_dep_courses:
      index = no_dep_courses.pop()
      course = graph[index]
      print(f"have course {index} and outnodes {course.out_nodes}")
      for prereq in course.out_nodes:
        graph[prereq].in_degrees -= 1       
        removed_edges += 1
        print(f"  removing edge from {index} to prereq {prereq}")
        if graph[prereq].in_degrees == 0:
          no_dep_courses.append(prereq)

    return removed_edges == total_deps

class GNode():
  def __init__(self):
    self.in_degrees = 0
    self.out_nodes = []



class Test(unittest.TestCase):
  def test_course_schedule(self):
    ts = Solution()

    trues =  [ (7, [[1,0], [2,0], [3,1], [4,1], [5,2], [6,2]] ), (1, [] ), (2, [[1,0]] ), (3, [[1,2],[2,0]])  ]
    falses = [ (4, [[2,0],[1,0],[3,1],[3,2],[1,3]] ), (2, [[1,0],[0,1]] ) ]

    #[ self.assertTrue(  ts.canFinish(n,courses) ) for n, courses in trues ]
    #[ self.assertTrue(  ts.can_finish_topo_sort(n,courses) ) for n, courses in trues ]
    [ self.assertTrue(  ts.can_finish_topo_sort2(n,courses) ) for n, courses in trues ]
    [ self.assertTrue(  ts.can_finish_dfs(n,courses) ) for n, courses in trues ]
    #[ self.assertFalse( ts.canFinish(n,courses) ) for n, courses in falses ]
    #[ self.assertFalse( ts.can_finish_topo_sort(n,courses) ) for n, courses in falses ]
    [ self.assertFalse( ts.can_finish_topo_sort2(n,courses) ) for n, courses in falses ]
    [ self.assertFalse( ts.can_finish_dfs(n,courses) ) for n, courses in falses ]

  def test_find_course_order(self):
    course_list = [[1,0]]
    course_list4 = [[1,0],[2,0],[3,1],[3,2]]
    course_list7 = [[1,0], [2,0], [3,1], [4,1], [5,2], [6,2] ]
    ts = Solution()
    self.assertEqual(ts.can_finish_topo_sort_find_order(2, course_list), [0,1] )
    self.assertEqual(ts.can_finish_topo_sort_find_order(4, course_list4), [0,1,2,3] )
    self.assertEqual(ts.can_finish_topo_sort_find_order(7, course_list7), [0,1,2,3,4,5,6] )

if __name__ == '__main__':
  unittest.main()
