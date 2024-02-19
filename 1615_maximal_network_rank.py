class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        connections = [0] * n
        directConnections = set()

        for x, y in roads:
            connections[x] += 1
            connections[y] += 1
            directConnections.add((x,y))
            directConnections.add((y,x))
        
        maxRank = 0

        for i in range(n):
            for j in range(i + 1, n):
                networkRank = connections[i] + connections[j]
                if (i, j) in directConnections:
                    networkRank -= 1

                maxRank = max(maxRank, networkRank)

        return maxRank
