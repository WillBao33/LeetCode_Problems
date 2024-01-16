class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        y = {}

        for i, x in enumerate(nums):
            diff = target - x

            if diff in y:
                return [y[diff],i]

            y[x] = i

        return None
        
