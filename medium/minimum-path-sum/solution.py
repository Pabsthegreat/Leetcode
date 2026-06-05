"""
[Description]
Minimum Path Sum
https://leetcode.com/problems/minimum-path-sum/

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 
Example 1:

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12

 
Constraints:

  m == grid.length
  n == grid[i].length
  1 <= m, n <= 200
  0 <= grid[i][j] <= 200

[Metadata]
- Difficulty: Medium
- Topics: Array, Dynamic Programming, Matrix
- Slug: minimum-path-sum
"""

// [Solution]
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [float('inf')]*n
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[j] = grid[i][j]
                elif j == 0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = grid[i][j] + min(dp[j],dp[j-1]) #dp[j] - above, dp[j-1] - left
        return dp[-1]
        # @lru_cache
        # def cost(i,j):
        #     c = grid[i][j]
        #     if i == m-1 and j == n-1:
        #         return c
        #     elif i == m-1:
        #         return c + cost(i,j+1)
        #     elif j == n-1:
        #         return c + cost(i+1,j)
        #     else:
        #         return c + min(cost(i,j+1),cost(i+1,j))
        # return cost(0,0)
