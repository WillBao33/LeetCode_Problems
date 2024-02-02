class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counts = defaultdict(int)
        max_length = left = 0

        for right, num in enumerate(nums):
            counts[num] += 1
            while counts[num] > k:
                counts[nums[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)

        return max_length
