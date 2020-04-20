#!/usr/bin/env python

import unittest

def max_duffel_bag_value(cake_tuples, weight_capacity):

    # Calculate the maximum value we can carry
    optimal_pack_by_remaining_weight = [0] * (weight_capacity +1) # initialize array of optimal values with a zero at array slot 0

    global_max = 0
    for weight in range(1, weight_capacity + 1):
        #print(f"checking weight {weight}")
        #print(f"with optimal pack {optimal_pack_by_remaining_weight}")
        local_max = 0
        for cake_weight, cake_value in cake_tuples:
            if cake_value <= 0:
                continue
            if cake_weight <= 0:
                return float("inf")
            #print(f"checking cake weight {cake_weight} value {cake_value}")
            if cake_weight <= weight:
                remaining_weight = weight - cake_weight
                #print(f"checking remaining {remaining_weight}")
                local_max  = max(local_max,  optimal_pack_by_remaining_weight[remaining_weight] + cake_value)
                global_max = max(global_max, local_max)
        optimal_pack_by_remaining_weight[weight] = local_max
    return global_max


# Tests

class Test(unittest.TestCase):
    """ https://www.interviewcake.com/question/python3/cake-thief
    Implement an optimal packing routine given a list of tuples of cakes.  Each contains 2 values (weight, value) """

    def test_one_cake(self):
        actual = max_duffel_bag_value([(2, 1)], 9)
        expected = 4
        self.assertEqual(actual, expected)

    def test_two_cakes(self):
        actual = max_duffel_bag_value([(4, 4), (5, 5)], 9)
        expected = 9
        self.assertEqual(actual, expected)

    def test_only_take_less_valuable_cake(self):
        actual = max_duffel_bag_value([(4, 4), (5, 5)], 12)
        expected = 12
        self.assertEqual(actual, expected)

    def test_lots_of_cakes(self):
        actual = max_duffel_bag_value([(2, 3), (3, 6), (5, 1), (6, 1), (7, 1), (8, 1)], 7)
        expected = 12
        self.assertEqual(actual, expected)

    def test_value_to_weight_ratio_is_not_optimal(self):
        actual = max_duffel_bag_value([(51, 52), (50, 50)], 100)
        expected = 100
        self.assertEqual(actual, expected)

    def test_zero_capacity(self):
        actual = max_duffel_bag_value([(1, 2)], 0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_cake_with_zero_value_and_weight(self):
        actual = max_duffel_bag_value([(0, 0), (2, 1)], 7)
        expected = 3
        self.assertEqual(actual, expected)

    def test_cake_with_non_zero_value_and_zero_weight(self):
        actual = max_duffel_bag_value([(0, 5)], 5)
        expected = float('inf')
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
