"""
[Description]
Special Positions in a Binary Matrix
https://leetcode.com/problems/special-positions-in-a-binary-matrix/

Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

 
Example 1:

Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

Example 2:

Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: (0, 0), (1, 1) and (2, 2) are special positions.

 
Constraints:

  m == mat.length
  n == mat[i].length
  1 <= m, n <= 100
  mat[i][j] is either 0 or 1.

[Metadata]
- Difficulty: Easy
- Topics: Array, Matrix
- Slug: special-positions-in-a-binary-matrix
"""

// [Solution]
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        l = len(mat[0])
        le = len(mat)
        r = []
        c = [0]*l
        for j in mat:
            s = 0
            for k in range(l):
                c[k]+= j[k]
                s+=j[k]
            r.append(s)
        count = 0
        for i in range(le):
            for j in range(l):
                if mat[i][j] == 1 and r[i] == 1 and c[j] == 1:
                    count += 1
        return count
