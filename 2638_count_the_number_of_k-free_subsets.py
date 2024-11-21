class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        chains = defaultdict(int)
        max_len = 0
        for num in nums:
            if num - k not in chains:
                chains[num] += 1
            else:
                chains[num] = chains[num - k] + 1
                del chains[num - k]
            max_len = max(max_len, chains[num])
        dp = [0] * max(2, max_len + 1)
        dp[0] = 1
        dp[1] = 2
        for i in range(2, max_len + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        return prod(map(lambda x: dp[x], chains.values())) 