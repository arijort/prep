#!/usr/bin/env python
import unittest
from collections import Counter
import heapq

class TempTracker(object):
    """ Implement a temperature tracker optimizing for fast retrieval of the max,min, mean and mode values. """ 
    # Implement methods to track the max, min, mean, and mode
    def __init__(self):
        self.max_val = float('-inf')
        self.min_val = float('inf')
        self.mode = None
        self.mean = None
        self._num_reads = 0
        self._total = 0
        self._val_counter = Counter()

    def insert(self, temperature):
        # mean
        self._num_reads += 1
        self._total += temperature
        self.mean = self._total / self._num_reads

        # max and min
        self.max_val = max( self.max_val, temperature)
        self.min_val = min( self.min_val, temperature)

        # mode
        self._val_counter[temperature] += 1
        self.mode = self._val_counter.most_common(1)[0][0]

    def get_max(self):
        return self.max_val

    def get_min(self):
        return self.min_val

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode


# Tests

class Test(unittest.TestCase):

    def test_tracker_usage(self):
        tracker = TempTracker()

        tracker.insert(50)
        msg = 'failed on first temp recorded'
        self.assertEqual(tracker.get_max(), 50, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 50.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 50, msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on higher temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 65.0, msg='mean ' + msg)
        self.assertIn(tracker.get_mode(), [50, 80], msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on third temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 70.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)

        tracker.insert(30)
        msg = 'failed on lower temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 30, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 60.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)

unittest.main(verbosity=2)
