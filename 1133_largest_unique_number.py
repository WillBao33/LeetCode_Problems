class Solution(object):
    def largestUniqueNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = defaultdict(int)
        ans = []

        for num in nums:
            counts[num] += 1

        for key in counts:
            if counts[key] == 1:
                ans.append(key)

        return -1 if not ans else max(ans)
