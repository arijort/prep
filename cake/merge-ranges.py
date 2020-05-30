#!/usr/bin/env python
import unittest

def merge_ranges(meetings):
    """ https://www.interviewcake.com/question/python3/merging-ranges
    Implement a mechanism to merge a set of merge_ranges.  Each is given as a tuple in a list. 
    e.g. [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)] 
    Return a list of merged ranges i.e.   [(0, 1), (3, 8), (9, 12)]
    """
    result_range = []
    meetings.sort()

    current_start = meetings[0][0]
    current_end   = meetings[0][1]
    for start, end in meetings[1:]:
        if start <= current_end: # continue the current range
            current_end = max(current_end, end)
        else: # current range has ended, start a new one
            result_range.append( (current_start, current_end) )
            current_start = start
            current_end   = end
    result_range.append( (current_start, current_end) )
    return result_range

# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_one_long_meeting_contains_smaller_meetings(self):
        actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
        expected = [(1, 12)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
