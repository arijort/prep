#!/usr/bin/env python
import unittest

def reverse(list_of_chars):
    """ https://www.interviewcake.com/question/cpp/reverse-string-in-place?course=fc1&section=array-and-string-manipulation
    Given a list of chars, reverse the list. Aim to minimize space requirements.

    Technique: 
      Given a string of length N in an array from 0 to N-1.
      Use a double pointer, one from front of the string, one from the end. Swap pairs of chars: (0, N-1), (1, N-2)
      Also use the technique in python where ~i will give the ith index from the end of the array.  Therefore we can swap chars [i] and [~i]
      >>> for n in range(5):
        ...   print(f"n is {n} complement is {~n}")
        ... 
        n is 0 complement is -1
        n is 1 complement is -2
        n is 2 complement is -3
        n is 3 complement is -4
        n is 4 complement is -5

    Time Complexity: O(n) since we are iterating over 0.5 of the string.
    Space Complexity: O(1) because we are using no extra space. We are replacing the string "in place".

    """
    # Reverse the input list of chars in place
    for i, char in enumerate(list_of_chars):
        if i > len(list_of_chars) // 2:
            break
        list_of_chars[i], list_of_chars[~i] = list_of_chars[~i], list_of_chars[i]

# Tests
class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)

unittest.main(verbosity=2)
