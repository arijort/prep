#!/usr/bin/env python

class Solution():
  def lengthOfLongestSubstring(self, s):
    """ return length of longest substring of unique values in the given string """
    if len(s) == 0:
      return 0
    maxl = 1
    # 2 pointer step through to show brute force implementation
    for i in range( len(s) - 1):
      print("running i %d" % i)
      ws = set() # working set of characters
      ws.add(s[i])
      for j in range( i + 1, len(s) ):
        print("running j %d" % j)
        if s[j] in ws:
          break
        else:
          ws.add(s[j])
      print("have ws length %d with max %d" % (len(ws), maxl))
      if len(ws) > maxl:
        maxl = len(ws)
    return maxl

def main():
  print("starting up")
  ts = Solution()
  res1 = ts.lengthOfLongestSubstring("abcabcbb")
  print("result 1 should be 3 : %d" % res1)
  res2 = ts.lengthOfLongestSubstring("bbbb")
  print("result 2 should be 1 : %d" % res2)
  res3 = ts.lengthOfLongestSubstring("au")
  print("result 3 should be 2 : %d" % res3)
  res4 = ts.lengthOfLongestSubstring("asdlfjkasdfoisdfjhqwerbaklsjdbfjklabsdflasjdfajsdjfbasdjbfljb2422bbasdbf")
  print("result 4 should be ? : %d" % res4)

if __name__ == '__main__':
  main()
