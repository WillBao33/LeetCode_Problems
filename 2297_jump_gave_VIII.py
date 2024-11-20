import math

class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        n = len(nums)
        increase_stack, decrease_stack, dp = [] * n, [] * n, [math.inf] * n
        dp[0] = 0


        for i in range(n):
            # downhill
            while decrease_stack and nums[decrease_stack[-1]] <= nums[i]:
                dp[i] = min(dp[i], dp[decrease_stack.pop()] + costs[i])

            # uphill
            while increase_stack and nums[increase_stack[-1]] > nums[i]:
                dp[i] = min(dp[i], dp[increase_stack.pop()] + costs[i])

            decrease_stack.append(i)
            increase_stack.append(i)

        return dp[-1]