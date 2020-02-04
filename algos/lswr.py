#!/usr/bin/env python

class Solution():
  def lengthOfLongestSubstring(self, s):
    """ return length of longest substring of unique values in the given string """
    if len(s) == 0:
      return 0
    max = 1
    # 2 pointer step through to show brute force implementation
    for i in range( len(s) - 1):
      ws = set() # working set of characters
      ws.add(s[i])
      for j in range( i + 1, len(s) - 1):
        if s[j] in ws:
          break
        else:
          ws.add(s[j])
      if len(ws) > max:
        max = len(ws)
    return max

def main():
  print("starting up")
  ts = Solution()
  res1 = ts.lengthOfLongestSubstring("abcabcbb")
  print("result 1 should be 3 : %d" % res1)
  res2 = ts.lengthOfLongestSubstring("bbbb")
  print("result 2 should be 1 : %d" % res2)

if __name__ == '__main__':
  main()
