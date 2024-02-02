class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = defaultdict(int)
        ans = 0

        for num in nums:
            counts[num] += 1

        max_freq = max(counts.values())
        for key in counts:
            if counts[key] == max_freq:
                ans += max_freq
        return ans
