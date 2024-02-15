class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def dfs(node):
            if not node:
                return None

            if val < node.val:
                return dfs(node.left)
            elif val > node.val:
                return dfs(node.right)
            elif val == node.val:
                return node

        return dfs(root)
