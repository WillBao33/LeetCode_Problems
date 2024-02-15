class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        indegree = [0]*n
        for _,y in edges:
            indegree[y] += 1

        return [node for node in range(n) if indegree[node] == 0]
