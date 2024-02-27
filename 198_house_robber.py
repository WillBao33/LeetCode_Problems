class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return max(nums)

        prev = nums[0]
        curr = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            temp = curr
            curr = max(curr, prev + nums[i])
            prev = temp

        return curr


    # def dp(i):
    #             if i < 0:
    #                 return 0
    
    #             if i in memo:
    #                 return memo[i]
    
    #             memo[i] = max(dp(i-1), dp(i-2)+nums[i])
    
    #             return memo[i]
    
    #         if not nums:
    #             return 0
    
    #         memo = {}
    #         return dp(len(nums)-1)
