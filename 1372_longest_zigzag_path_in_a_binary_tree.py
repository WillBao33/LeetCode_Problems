class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.pathLength = 0

        def dfs(node,left, length):
            if not node:
                return 0

            self.pathLength = max(self.pathLength, length)
            if left:
                dfs(node.left,False,length + 1)
                dfs(node.right, True, 1)
            else:
                dfs(node.left,False,1)
                dfs(node.right,True, length + 1)

        dfs(root, False, 0)
        dfs(root, True, 0)
        return self.pathLength
