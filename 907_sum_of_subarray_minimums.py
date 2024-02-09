class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack = deque()
        ans = 0 
        MOD = 10**9 + 7
        arr = [0] + arr + [0]
        for i, num in enumerate(arr):
            while stack and num < arr[stack[-1]]:
                idx = stack.pop()
                ans += arr[idx]*(i - idx)*(idx - stack[-1])
                ans %= MOD

            stack.append(i)

        return ans
