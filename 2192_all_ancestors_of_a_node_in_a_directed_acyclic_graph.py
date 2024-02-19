class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        ancestors = defaultdict(set)
        for x, y in edges:
            ancestors[y].add(x)

        ans = [set() for _ in range(n)]
        def dfs(node, current):
            if ans[node]:
                return 

            for ancestor in ancestors[node]:
                ans[node].add(ancestor)
                dfs(ancestor, node)
                ans[node] = ans[node].union(ans[ancestor])

        for i in range(n):
            dfs(i, None)

        return [sorted(list(ancestor_set)) for ancestor_set in ans]
