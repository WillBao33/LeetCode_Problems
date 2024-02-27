class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp = [amount + 1] * (amount + 1)
        # dp[0] = 0

        # for i in range(1, amount + 1):
        #     for coin in coins:
        #         if coin <= i:
        #             dp[i] = min(dp[i], dp[i-coin]+1)

        # return dp[amount] if dp[amount] != amount + 1 else -1

        @cache
        def dp(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return -1

            min_count = float('inf')
            for coin in coins:
                res = dp(rem - coin)
                if res >=0 and res < min_count:
                    min_count = res + 1

            return min_count if min_count != float('inf') else -1

        return dp(amount)
