import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        ans = 0
        for i in range(k):
            ans = heapq.heappop(heap)

        return -ans
