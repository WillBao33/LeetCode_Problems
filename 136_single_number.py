from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = Counter(nums)
        for key, value in nums.items():
            if value == 1:
                return key
