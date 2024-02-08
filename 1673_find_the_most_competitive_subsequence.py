class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # using a increaing monotonic stack
        # iterate through nums, pop top when a smaller number encountered comparing to stack[-1] 
        stack = deque()
        for i, num in enumerate(nums):
            while stack and stack[-1] > num and len(stack) - 1 + len(nums) - i >= k:
                stack.pop()

            if len(stack) < k:
                stack.append(num)


        return stack
