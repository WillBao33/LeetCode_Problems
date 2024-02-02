class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_dict = defaultdict(int)
        ans = 0

        for num in nums:
            my_dict[num] += 1

        for key in my_dict:
            if my_dict[key] > 1:
                ans += (my_dict[key] * (my_dict[key]-1))/2

        return ans
