class Solution(object):
    def reachableNodes(self, n, edges, restricted):
        """
        :type n: int
        :type edges: List[List[int]]
        :type restricted: List[int]
        :rtype: int
        """
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        seen = set(restricted)
        seen.add(0)

        def dfs(node):
            ans = 1
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    ans += dfs(neighbor)
            return ans

        return dfs(0)
