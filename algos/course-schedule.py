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
      #adj_list[course].append(prereq)
      if not start_course:
        start_course = course
    print(f"made course_dict {course_dict}")

        

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

    trues =  [ (1, [] ), (2, [[1,0]] ), (3, [[1,2],[2,0]])  ]
    falses = [ (4, [[2,0],[1,0],[3,1],[3,2],[1,3]] ), (2, [[1,0],[0,1]] ) ]

    #[ self.assertTrue(  ts.canFinish(n,courses) ) for n, courses in trues ]
    [ self.assertTrue(  ts.can_finish_topo_sort(n,courses) ) for n, courses in trues ]
    #[ self.assertFalse( ts.canFinish(n,courses) ) for n, courses in falses ]
    [ self.assertFalse( ts.can_finish_topo_sort(n,courses) ) for n, courses in falses ]

if __name__ == '__main__':
  unittest.main()
