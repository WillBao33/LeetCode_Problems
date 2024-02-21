from collections import defaultdict
import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        head_workers = costs[:candidates]
        tail_workers = costs[max(candidates,len(costs)-candidates):]
        heapq.heapify(head_workers)
        heapq.heapify(tail_workers)

        ans = 0
        next_head = candidates
        next_tail = len(costs) - candidates - 1
        for _ in range(k):
            if not tail_workers or head_workers and head_workers[0] <= tail_workers[0]:
                ans += heapq.heappop(head_workers)

                if next_head <= next_tail:
                    heapq.heappush(head_workers,costs[next_head])
                    next_head += 1
            else:
                ans += heapq.heappop(tail_workers)
                
                if next_head <= next_tail:
                    heapq.heappush(tail_workers,costs[next_tail])
                    next_tail -= 1

        return ans
