class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        queue = deque()
        for i in range(len(nums)):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            if queue[0] + k == i:
                queue.popleft()

            if i >= k - 1:
                ans.append(nums[queue[0]])

        return ans
