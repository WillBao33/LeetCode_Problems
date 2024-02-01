class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) + 1
        numbers = set(range(n))
        
        for num in nums:
            numbers.discard(num)
        return numbers.pop()
