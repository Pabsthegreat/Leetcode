"""
[Description]
Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

 
Constraints:

  1 <= prices.length <= 105
  0 <= prices[i] <= 104

[Metadata]
- Difficulty: Easy
- Topics: Array, Dynamic Programming
- Slug: best-time-to-buy-and-sell-stock
"""

// [Solution]
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        p0 = 0
        price = 0
        p1 = 0
        temp = 0
        for i in range(len(prices)):
            if prices[i] < prices[p0]:
                p0 = i
                p1 = i
                if temp > price:
                    price = temp
                temp = 0
            if prices[i] > prices[p1]:
                p1 = i
                temp = prices[p1] - prices[p0]
        if temp > price:
            return temp
        return price