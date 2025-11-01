class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = prices[0]
        for i in prices:
            if i > min_price:
                max_profit = max_profit + i - min_price 
                min_price = i
            if i < min_price:
                min_price = i 
        return max_profit