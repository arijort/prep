#!/usr/bin/env python
import unittest

class Solution():
  def licenseKeyFormatting(self, S: str, K: int) -> str:
    buf,result = [], []
    S = S.replace("-", "")
    for char in S.upper():
      if char.isalnum():
        buf.append(char)
    if len(S) == 0:
      return ""
    leftover = len(buf) % K
    if leftover == 0:
      leftover = K
    print(f"leftover is {leftover}")
    if leftover == len(buf):
      return "".join(buf[0:leftover])
    result = buf[0:leftover]
    buf = buf[leftover:]
    remnants = [ "".join(buf[i*K: (i+1) * K]) for i in range(len(buf) // K) ]
    return "".join(result) + "-" + "-".join(remnants)

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
