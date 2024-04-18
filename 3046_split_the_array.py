class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        for val in counts.values():
            if val > 2:
                return False

        return True
