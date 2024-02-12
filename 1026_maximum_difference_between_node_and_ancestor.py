# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, curr_max, curr_min):
            if not node:
                return curr_max - curr_min

            curr_max = max(curr_max, node.val)
            curr_min = min(curr_min, node.val)
            left = dfs(node.left, curr_max, curr_min)
            right = dfs(node.right, curr_max, curr_min)
            return max(left,right)
            
        return dfs(root,root.val, root.val)
