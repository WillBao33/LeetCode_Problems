class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        seen = set()

        def dfs(node):
            if node == destination:
                return True
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen and dfs(neighbor):
                    return True
            return False

        return dfs(source)
