# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node,curr_max):
            if not node:
                return 0

            left = dfs(node.left, max(curr_max,node.val))
            right = dfs(node.right, max(curr_max, node.val))
            ans = left + right
            if node.val >= curr_max:
                ans += 1

            return ans

        return dfs(root, float('-inf'))
