#!/usr/bin/env python
import unittest

class Solution():
  def maximal_square(self, matrix):
    maxarea, maxside = 0,0
    matrix_rows = len(matrix)
    if not matrix_rows:
      return 0
    matrix_cols = len(matrix[0])
    for i, row in enumerate(matrix):
      if matrix_rows - maxside <= i:
        break
      for j, col in enumerate(row):
        if matrix_cols - maxside <= j:
          break
        if matrix[i][j] == "1":
          have_square = True
          maxside = max(1, maxside)
          side = maxside
          while side < matrix_rows - i and side < matrix_cols - j:
            if matrix[i+side][j+side] != "1":
              have_square == False
              break
            if not all( [ matrix[i+side][jprime] == "1" for jprime in range(j+side,j-1,-1 )]): # check row i+sid
              have_square == False
              break
            if not all( [ matrix[iprime][j+side] == "1" for iprime in range(i+side,i-1,-1 )]): # check row i+sid
              have_square == False
              break
            side += 1
          if have_square:
            maxside = max(maxside, side)
            print(f"setting maxside to {maxside}")
    return maxside ** 2

class Test(unittest.TestCase):
  def test_maximal_square(self):
    ts = Solution()
    a = [ ["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"] ]

    self.assertEqual(ts.maximal_square(a), 4)

if __name__ == '__main__':
  unittest.main()
