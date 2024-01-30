class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        total_sum = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == (total_sum - num - left_sum):
                return i
            left_sum += num

        return -1
