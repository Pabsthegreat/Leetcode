"""
[Description]
N-Queens II
https://leetcode.com/problems/n-queens-ii/

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 
Example 1:

Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:

Input: n = 1
Output: 1

 
Constraints:

  1 <= n <= 9

[Metadata]
- Difficulty: Hard
- Topics: Backtracking
- Slug: n-queens-ii
"""

// [Solution]
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        col = set()
        pos = set()  # row + col
        neg = set()  # row - col

        def backtrack(row):
            if row == n:
                self.count += 1
                return
            
            for c in range(n):
                if c in col or (row + c) in pos or (row - c) in neg:
                    continue

                col.add(c)
                pos.add(row + c)
                neg.add(row - c)

                backtrack(row + 1)

                col.remove(c)
                pos.remove(row + c)
                neg.remove(row - c)

        backtrack(0)
        return self.count