import heapq
class Solution(object):
    def halveArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        half_sum = sum(nums) / 2.0
        heap = [-num for num in nums]
        heapq.heapify(heap)
        ans = 0
        while half_sum > 0:
            ans += 1
            x = heapq.heappop(heap)
            half_sum += x / 2.0
            heapq.heappush(heap, x/2.0)

        return ans
