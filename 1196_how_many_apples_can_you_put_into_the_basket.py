class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        limit = 5000
        ans = 0
        for apple in weight:
            if apple <= limit:
                ans += 1
                limit -= apple
            else:
                return ans

        return ans
