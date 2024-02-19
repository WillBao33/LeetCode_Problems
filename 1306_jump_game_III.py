class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])
        seen = {start}

        while queue:
            node = queue.popleft()
            if arr[node] == 0:
                return True

            for i in [-1, 1]:
                new_node = node + i*arr[node]
                if new_node not in seen and 0 <= new_node < len(arr):
                    seen.add(new_node)
                    queue.append(new_node)

        return False
