"""
[Description]
Coin Change
https://leetcode.com/problems/coin-change/

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 
Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0

 
Constraints:

  1 <= coins.length <= 12
  1 <= coins[i] <= 231 - 1
  0 <= amount <= 104

[Metadata]
- Difficulty: Medium
- Topics: Array, Dynamic Programming, Breadth-First Search
- Slug: coin-change
"""

// [Solution]
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        best = {}
        def dfs(amt):
            if amt == 0:
                return 0
            if amt < 0:
                return float('inf')
            if amt in best:
                return best[amt]
            b = float('inf')
            for coin in coins:
                b = min(1+dfs(amt-coin),b)
            best[amt] = b
            return b
        ans = dfs(amount)    
        if ans == float('inf'):
            return -1
        return ans   
