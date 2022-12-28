#!/usr/bin/env python
import unittest
from typing import List

class Solution():
  def letterCombinations(self, digits:str) -> List[str]:
    # https://leetcode.com/problems/letter-combinations-of-a-phone-number/
    mapd = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz' }
    result = []
    if not digits:
      return result
    if len(digits) == 1:
      return list( mapd[digits[0]] )
    for prefix in mapd[digits[0]]:
      for suffix in self.letterCombinations(digits[1:] ):
       result.append( prefix + suffix)
    return result


  def lc2(self, digits:str) -> List[str]:
    dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz' }
    def dfs(index, path):
      if(len(path) == len(digits)):
        result.append(path)
        return
      for i in range(index, len(digits)):
        for j in dic[digits[i]]:
          dfs(i+1, path+j)

    if not digits:
      return []
    result = []
    dfs(0,'')
    return result

class Test(unittest.TestCase):
  def test_foo(self):
    ts = Solution()
    self.assertEqual(ts.letterCombinations("23"), ["ad","ae","af","bd","be","bf","cd","ce","cf"] )
    self.assertEqual(ts.letterCombinations("5"), ['j','k','l'])
    self.assertEqual(ts.letterCombinations("6"), ['m','n','o'])
    self.assertEqual(ts.letterCombinations("7"), ['p','q','r','s'])
    self.assertEqual(ts.letterCombinations("9"), ['w','x','y','z'])
    self.assertEqual(ts.letterCombinations("8"), ['t','u','v'])
    self.assertEqual(ts.letterCombinations("49"), ["gw","gx","gy","gz","hw","hx","hy","hz","iw","ix","iy","iz"] )
    self.assertEqual(ts.letterCombinations("57"), ['jp','jq','jr','js','kp','kq','kr','ks','lp','lq','lr','ls'])

    self.assertEqual(ts.letterCombinations(""), [])

    ts2 = Solution()
    self.assertEqual(ts2.lc2("57"), ['jp','jq','jr','js','kp','kq','kr','ks','lp','lq','lr','ls'])


    self.assertTrue(True)
    pass

if __name__ == '__main__':
  unittest.main()
