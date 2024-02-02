class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        counts = defaultdict(int)
        counts[0] = 1

        ans = curr = 0

        for num in nums:
            curr += num
            if curr - goal in counts:
                ans += counts[curr - goal]

            counts[curr] += 1

        return ans
