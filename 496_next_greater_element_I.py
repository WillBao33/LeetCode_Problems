class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        queue = deque()
        next_greater = {}
        for num in nums2:
            while queue and queue[-1] < num:
                next_greater[queue.pop()] = num
            queue.append(num)

        for num in queue:
            next_greater[num] = -1

        ans = [next_greater[num] for num in nums1]
        return ans
