class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix = [nums[0]]
        for num in nums:
            self.prefix.append(num + self.prefix[-1])
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefix[right+1] - self.prefix[left]
