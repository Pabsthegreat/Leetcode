"""
[Description]
Climbing Stairs
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

 
Constraints:

  1 <= n <= 45

[Metadata]
- Difficulty: Easy
- Topics: Math, Dynamic Programming, Memoization
- Slug: climbing-stairs
"""

// [Solution]
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        
        a, b = 1, 1  # dp[0], dp[1]
        for i in range(2, n + 1):
            a, b = b, a + b  # shift window forward
        
        return b

        
    # class Solution:
    # def climbStairs(self, n: int) -> int:
    #     memo = {}
        
    #     def dp(i):
    #         if i == 0 or i == 1:
    #             return 1
    #         if i in memo:
    #             return memo[i]
    #         memo[i] = dp(i - 1) + dp(i - 2)
    #         return memo[i]
        
    #     return dp(n)