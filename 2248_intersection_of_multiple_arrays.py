from collections import defaultdict
class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        counts = defaultdict(int)
        ans = []
        for arr in nums:
            for x in arr:
                counts[x] += 1
        n = len(nums)
        for key in counts:
            if counts[key] == n:
                ans.append(key)

        return sorted(ans)
