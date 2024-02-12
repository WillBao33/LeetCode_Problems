# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        if not root.left:
            right = self.minDepth(root.right)
            return right + 1
        elif not root.right:
            left = self.minDepth(root.left)
            return left + 1
        else:
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            return min(left,right) + 1
