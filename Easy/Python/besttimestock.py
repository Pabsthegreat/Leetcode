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
    
# Optimal:
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         min_price = float('inf')
#         max_profit = 0
        
#         for price in prices:
#             if price < min_price:
#                 min_price = price
#             else:
#                 max_profit = max(max_profit, price - min_price)
                
#         return max_profit
