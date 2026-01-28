"""
[Description]
Spiral Matrix
https://leetcode.com/problems/spiral-matrix/

Given an m x n matrix, return all elements of the matrix in spiral order.

 
Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

 
Constraints:

  m == matrix.length
  n == matrix[i].length
  1 <= m, n <= 10
  -100 <= matrix[i][j] <= 100

[Metadata]
- Difficulty: Medium
- Topics: Array, Matrix, Simulation
- Slug: spiral-matrix
"""

// [Solution]
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = len(matrix)
        m = len(matrix[0])
        top, bottom = 0, n - 1
        left, right = 0, m - 1
        l = []
        while top <= bottom and left <= right:
            # Right
            for i in range(left, right+1):
                l.append(matrix[top][i])
            top += 1
            
            # Down
            for i in range(top, bottom+1):
                l.append(matrix[i][right])
            right -= 1
            
            # Left (only if there are rows remaining)
            if top <= bottom:#imp check
                for i in range(right, left-1, -1):
                    l.append(matrix[bottom][i])
                bottom -= 1
            
            # Up (only if there are columns remaining)
            if left <= right:#imp check
                for i in range(bottom, top-1, -1):
                    l.append(matrix[i][left])
                left += 1
        return l