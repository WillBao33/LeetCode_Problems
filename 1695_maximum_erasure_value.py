class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_sum = [0,nums[0]]
        ans = 0
        counts = defaultdict(int)
        start = 0
        
        for i in range(1,len(nums)):
            prefix_sum.append(nums[i]+prefix_sum[-1])

        for i, num in enumerate(nums):
            if num in counts and counts[num] >= start:
                ans = max(ans,prefix_sum[i]-prefix_sum[start])
                start = counts[num] + 1
            
            counts[num] = i
        ans = max(ans,prefix_sum[-1]-prefix_sum[start])

        return ans
