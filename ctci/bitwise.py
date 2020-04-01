#!/usr/bin/env python
import unittest


def find_unique_delivery_id(delivery_ids):
    """ https://www.interviewcake.com/question/python3/find-unique-int-among-duplicates
    Implement a technique for discover which of many id values appear only once in a list.  All other will appear twice. """
    # Find the one unique ID in the list
    result = 0
    for id in delivery_ids:
        result ^= id 
    return result

# Tests

class Test(unittest.TestCase):

    def test_one_drone(self):
        actual = find_unique_delivery_id([1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_unique_id_comes_first(self):
        actual = find_unique_delivery_id([1, 2, 2])
        expected = 1
        self.assertEqual(actual, expected)

    def test_unique_id_comes_last(self):
        actual = find_unique_delivery_id([3, 3, 2, 2, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_unique_id_in_middle(self):
        actual = find_unique_delivery_id([3, 2, 1, 2, 3])
        expected = 1
        self.assertEqual(actual, expected)

    def test_many_drones(self):
        actual = find_unique_delivery_id([2, 5, 4, 8, 6, 3, 1, 4, 2, 3, 6, 5, 1])
        expected = 8
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
