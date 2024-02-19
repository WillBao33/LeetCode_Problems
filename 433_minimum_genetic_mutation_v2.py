from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1

        bank = set(bank)  # Convert bank to a set for O(1) lookups
        forward_queue = deque([(startGene, 0)])
        backward_queue = deque([(endGene, 0)])
        forward_seen = {startGene: 0}
        backward_seen = {endGene: 0}

        while forward_queue and backward_queue:
            fwd_res = self.bfs_step(forward_queue, bank, forward_seen, backward_seen)
            if fwd_res is not None:
                return fwd_res
            bwd_res = self.bfs_step(backward_queue, bank, backward_seen, forward_seen)
            if bwd_res is not None:
                return bwd_res

        return -1

    def bfs_step(self, queue, bank, seen_self, seen_other):
        node, steps = queue.popleft()
        for c in "ACGT":
            for i in range(len(node)):
                neighbor = node[:i] + c + node[i+1:]
                if neighbor in seen_other:
                    # When the two searches meet, return the sum of steps from both sides
                    return steps + 1 + seen_other[neighbor]
                if neighbor in bank and neighbor not in seen_self:
                    seen_self[neighbor] = steps + 1
                    queue.append((neighbor, steps+1))
        return None
