class Solution(object):
    def validSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        stack = deque()

        for i, num in enumerate(nums):
            while stack and num < nums[stack[-1]]:
                idx = stack.pop()
                ans += i - idx
            stack.append(i)

        while stack:
            idx = stack.pop()
            ans += len(nums) - idx

        return ans
