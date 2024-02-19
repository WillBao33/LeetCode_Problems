class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        graph = [[] for _ in range(26)]

        def dfs(node, label):
            component[node] = label
            for neighbor in graph[node]:
                if component[neighbor] == -1:
                    dfs(neighbor, label)

        for eq in equations:
            if eq[1] == '=':
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                graph[x].append(y)
                graph[y].append(x)


        component = [-1] * 26
        label = 0
        for i in range(26):
            if component[i] == -1:
                dfs(i, label)
                label += 1

        for eq in equations:
            if eq[1] == '!':
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                if component[x] == component[y]:
                    return False

        return True
