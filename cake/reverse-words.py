#!/usr/bin/env python
import unittest

def reverse_words(message):
    """ https://www.interviewcake.com/question/python3/reverse-words
    Given a string, reverse all the words in the string.

    Technique: First reverse the entire string
      Second iterate over the words reversing the letters of each word.

    Time Complexity: O(N) we are reversing the entire string for N, then reverse each word which goes over N a second time.
    Space Complexity: O(1) constant space because we are replacing the words in place.
    """

    # Decode the message by reversing the words
    # 
    reverse(message, 0, len(message) - 1)
    word_start = 0
    for i,c in enumerate(message):
        if c == ' ':
            reverse(message, word_start, i-1)
            word_start = i+1
    reverse(message, word_start, len(message)-1) # do last word

def reverse(list_of_chars, start, end):
    # Reverse the input list of chars in place
    while start < end:
        list_of_chars[start], list_of_chars[end] = list_of_chars[end], list_of_chars[start]
        start += 1
        end -= 1
    #for i, char in enumerate(list_of_chars[start:end]):
    # //   if i > len(list_of_chars[start:end]) // 2:
    #  //      break
    #   // list_of_chars[i], list_of_chars[~i] = list_of_chars[~i], list_of_chars[i]

# Tests
class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)
    def test_spacy_string(self):
        message = list(' foo ')
        reverse_words(message)
        expected = list(' foo ')
        self.assertEqual(message, expected)

unittest.main(verbosity=2)
