class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.closest = root.val
        def dfs(node):
            if not node:
                return 
            if abs(node.val - target) < abs(self.closest - target):
                self.closest = node.val
            elif abs(node.val - target) == abs(self.closest - target):
                self.closest = min(node.val, self.closest)

            if target < node.val:
                dfs(node.left)
            elif target > node.val:
                dfs(node.right)

        dfs(root)

        return self.closest
