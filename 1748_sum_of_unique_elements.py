class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = defaultdict(int)
        ans = 0
        for num in nums:
            counts[num] += 1

        for key in counts:
            if counts[key] == 1:
                ans += key

        return ans
