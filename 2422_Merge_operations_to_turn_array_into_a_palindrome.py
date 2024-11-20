class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # two pointers
        left, right = 0, len(nums) - 1
        operations = 0

        while left < right:
            if nums[left] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] < nums[right]:
                nums[left + 1] += nums[left]
                left += 1
                operations += 1
            else:
                nums[right - 1] += nums[right]
                right -= 1
                operations += 1

        return operations
