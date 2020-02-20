#!/usr/bin/env python

class Solution():
  def isBadVersion(self, version):
    return version >= 12

  def firstBadVersion(self, n):
    """ Given int n, a number of commits and method isBadVersion() return int the initial bad commit in a code repo, minimizing the number of calls to isBadversion. """ 
    print("given version n %d" % n)
    mid = n // 2;
    found = False
    lo, hi = 1, n
    while not mid == lo and not mid == hi:
      #print("checking version %d with lo %d hi %d" % (mid, lo, hi))
      if self.isBadVersion(mid):
        hi = mid
        mid = (hi + lo) // 2
        found = True
      else:
        lo = mid
        mid = (hi + lo) //2

      print("ending with mid %d with lo %d hi %d" % (mid, lo, hi))
    return hi if found else -1

def main():
  print("starting up ")
  ts = Solution()
  print("found first bad version %d" % ts.firstBadVersion(30))
  print("found first bad version %d" % ts.firstBadVersion(15))
  print("found first bad version %d" % ts.firstBadVersion(12))
  print("found first bad version %d" % ts.firstBadVersion(2))

if __name__ == '__main__':
  main()
