"""
[Description]
Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/

You are given an m x n integer matrix matrix with the following two properties:

  Each row is sorted in non-decreasing order.
  The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 
Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

 
Constraints:

  m == matrix.length
  n == matrix[i].length
  1 <= m, n <= 100
  -104 <= matrix[i][j], target <= 104

[Metadata]
- Difficulty: Medium
- Topics: Array, Binary Search, Matrix
- Slug: search-a-2d-matrix
"""

// [Solution]
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = rows * cols - 1

        while l <= r:
            mid = (l + r) // 2

            row = mid // cols
            col = mid % cols

            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1

        return False