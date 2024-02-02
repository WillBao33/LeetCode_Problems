class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        counts = defaultdict(int)

        for num in nums:
            if num in counts:
                return True
            else:
                counts[num] += 1
        return False
