class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        inc_queue = deque()
        dec_queue = deque()
        left = ans = 0
        for right in range(len(nums)):
            while inc_queue and inc_queue[-1] > nums[right]:
                inc_queue.pop()
            while dec_queue and dec_queue[-1] < nums[right]:
                dec_queue.pop()

            inc_queue.append(nums[right])
            dec_queue.append(nums[right])

            while dec_queue[0] - inc_queue[0] > limit:
                if nums[left] == dec_queue[0]:
                    dec_queue.popleft()
                if nums[left] == inc_queue[0]:
                    inc_queue.popleft()

                left += 1
            ans = max(ans,right - left + 1)
        return ans
