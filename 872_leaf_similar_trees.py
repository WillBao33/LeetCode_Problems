class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return []

            if not node.left and not node.right:
                return [node.val]
            return dfs(node.left) + dfs(node.right)

        leaves1 = dfs(root1)
        leaves2 = dfs(root2)

        return leaves1 == leaves2
