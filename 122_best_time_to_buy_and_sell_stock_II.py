class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        local_min = prices[0]
        local_max = prices[0]
        max_profit = 0

        i = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i+1]:
                i += 1
            local_min = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i+1]:
                i += 1
            local_max = prices[i]
            
            max_profit += local_max - local_min

        return max_profit
