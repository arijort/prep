#!/usr/bin/env python
import unittest

from collections import deque

def get_path(graph, start_node, end_node):

    # Find the shortest route in the network between the two users

    # 1 create queue
    if not start_node in graph or not end_node in graph:
        raise Exception

    q = deque()
    q.append(start_node)
    return bfs(graph, start_node, end_node)

def reconstruct_path(path_dict):
    print(f"dict of paths {path_dict}")

def bfs(graph, start_node, end_node ):
    """ bfs implementation that returns node on the path to the target.  If it revisits a node, return None. """
    q = deque()
    q.append(start_node)
    path_to = { start_node: None}
    found = False
    while len(q) > 0:
        node = q.popleft()
        if node == end_node:
            found = True
            break
        for neighbor in graph[node]:
           if neighbor not in path_to:
               q.append(neighbor)
               path_to[neighbor] = node

    if not found:
        return None
    runner = end_node
    result = []
    print(path_to)
    while runner:
        print(f"handling runner {runner} have path to {path_to[runner]}")
        result.append(runner)
        runner = path_to[runner]
    print(f"returning f{result}")
    return result[::-1]
# Tests

class Test(unittest.TestCase):

    def setUp(self):
        self.graph = {
            'a': ['b', 'c', 'd'],
            'b': ['a', 'd'],
            'c': ['a', 'e'],
            'd': ['a', 'b'],
            'e': ['c'],
            'f': ['g'],
            'g': ['f'],
        }

    def test_two_hop_path_1(self):
        actual = get_path(self.graph, 'a', 'e')
        expected = ['a', 'c', 'e']
        self.assertEqual(actual, expected)

    def test_two_hop_path_2(self):
        actual = get_path(self.graph, 'd', 'c')
        expected = ['d', 'a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_1(self):
        actual = get_path(self.graph, 'a', 'c')
        expected = ['a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_2(self):
        actual = get_path(self.graph, 'f', 'g')
        expected = ['f', 'g']
        self.assertEqual(actual, expected)

    def test_one_hop_path_3(self):
        actual = get_path(self.graph, 'g', 'f')
        expected = ['g', 'f']
        self.assertEqual(actual, expected)

    def test_zero_hop_path(self):
        actual = get_path(self.graph, 'a', 'a')
        expected = ['a']
        self.assertEqual(actual, expected)

    def test_no_path(self):
        actual = get_path(self.graph, 'a', 'f')
        expected = None
        self.assertEqual(actual, expected)

    def test_start_node_not_present(self):
        with self.assertRaises(Exception):
            get_path(self.graph, 'h', 'a')

    def test_end_node_not_present(self):
        with self.assertRaises(Exception):
            get_path(self.graph, 'a', 'h')


unittest.main(verbosity=2)
