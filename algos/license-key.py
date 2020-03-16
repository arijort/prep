#!/usr/bin/env python
import unittest

class Solution():
  def licenseKeyFormatting(self, S: str, K: int) -> str:
    buf,result = [], []
    S = S.upper().replace("-", "")
    leftover = len(S) % K
    if leftover:
      result.append( S[:leftover] )
    print(f"leftover is {leftover}")
    if leftover == len(S):
      return "".join(S[0:leftover])
    [ result.append(S[i:i+K]) for i in range(leftover, len(S), K) ]
    print(f"result is {result}")
    return "-".join(result)

class Test(unittest.TestCase):
  def test_foo(self):
    ts = Solution()

    self.assertEqual( ts.licenseKeyFormatting("5F3Z-2e-9-w", 4), "5F3Z-2E9W" )
    self.assertEqual( ts.licenseKeyFormatting("5F3Z-2e-9-waadsf-asdf8987-ads9f8asf", 4), "5F-3Z2E-9WAA-DSFA-SDF8-987A-DS9F-8ASF" )
    self.assertEqual( ts.licenseKeyFormatting("5F3Z-2e-9-waadsf-asdf8987-ads9f8asf", 5), "5F3Z2-E9WAA-DSFAS-DF898-7ADS9-F8ASF" )
    self.assertEqual( ts.licenseKeyFormatting("r", 1), "R")
    self.assertEqual( ts.licenseKeyFormatting("---", 3), "")

if __name__ == '__main__':
  unittest.main()
