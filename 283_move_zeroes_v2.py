class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr = 0
        for num in nums:
            if num != 0:
                nums[curr] = num
                curr += 1
        for i in range(curr, len(nums)):
            nums[i] = 0
