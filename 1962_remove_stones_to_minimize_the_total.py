import math
import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        stones = [-stone for stone in piles]
        heapq.heapify(stones)
        for i in range(k):
            x = heapq.heappop(stones)
            x -= -math.floor(-x / 2)
            heapq.heappush(stones, x)

        return abs(sum(stones))
