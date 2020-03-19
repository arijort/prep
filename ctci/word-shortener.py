#!/usr/bin/env python
import unittest
from pprint import pprint as pp

class Trie(object):
    # Implement a trie and use it to efficiently store strings
    def __init__(self):
        self.root = dict()
        self.end_mark = "END"

    def add_word(self, word):
        d = self.root
        pp(d)
        is_new = False
        for char in word:
            print(f"  doing char {char}")
            if not char in d:
                print(f"    did not find char {char}")
                d[char] = dict()
                is_new = True
            d = d[char]
        if self.end_mark not in d:
            is_new = True
            d[self.end_mark] = {}
        return is_new

# Tests
class Test(unittest.TestCase):

    def test_trie_usage(self):
        trie = Trie()

        result = trie.add_word('catch')
        self.assertTrue(result, msg='new word 1')

        result = trie.add_word('cakes')
        self.assertTrue(result, msg='new word 2')

        result = trie.add_word('cake')
        self.assertTrue(result, msg='prefix of existing word')

        result = trie.add_word('cake')
        self.assertFalse(result, msg='word already present')

        result = trie.add_word('caked')
        self.assertTrue(result, msg='new word 3')

        result = trie.add_word('catch')
        self.assertFalse(result, msg='all words still present')

        result = trie.add_word('')
        self.assertTrue(result, msg='empty word')

        result = trie.add_word('')
        self.assertFalse(result, msg='empty word present')

unittest.main(verbosity=2)
