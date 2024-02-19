from math import sqrt
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(bombs)):
            x1, y1, r1 = bombs[i]
            for j, item in enumerate(bombs):
                if i != j:
                    x2, y2, r2 = bombs[j]
                    d = sqrt((x2-x1)**2 + (y2-y1)**2)
                    if r1 >= d:
                        graph[i].append(j)

        def dfs(start):
            queue = deque([start])
            seen = {start}

            while queue:
                bomb = queue.popleft()
                for next_bomb in graph[bomb]:
                    if next_bomb not in seen:
                        seen.add(next_bomb)
                        queue.append(next_bomb)

            return len(seen)
        max_detonated = 0
        for i in range(len(bombs)):
            max_detonated = max(max_detonated, dfs(i))

        return max_detonated
