class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        prefix = [0]
        ans = [-1]*n
        for num in nums:
            prefix.append(prefix[-1] + num)
            
        for i in range(n):
            if i - k >= 0 and i + k < n:
                subarray_sum = prefix[i+k+1] - prefix[i-k]
                ans[i] = subarray_sum // (2*k+1)
                
        return ans
