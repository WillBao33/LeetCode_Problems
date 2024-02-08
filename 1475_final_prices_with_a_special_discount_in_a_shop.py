class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        queue = deque()
        ans = prices[:]
        curr = 0

        for i, price in enumerate(prices):
            while queue and prices[queue[-1]] >= price:
                index = queue.pop()
                ans[index] = prices[index] - price
            queue.append(i)

        return ans
