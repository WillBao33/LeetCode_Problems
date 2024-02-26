class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def backtrack(node, path):
            if node == len(graph) - 1:
                paths.append(list(path))
                return 

            for next_node in graph[node]:
                path.append(next_node)
                backtrack(next_node,path)
                path.pop()

        paths = []
        backtrack(0,[0])
        return paths
