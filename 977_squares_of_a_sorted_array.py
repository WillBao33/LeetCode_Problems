class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = [0]*len(nums)
        i = 0
        j = len(nums) - 1
        k = len(nums) - 1
        
        while i <= j:
            if abs(nums[i]) < abs(nums[j]):
                arr[k] = nums[j] ** 2
                j -= 1
            else:
                arr[k] = nums[i] ** 2
                i += 1
            k -= 1
                
        return arr
        
