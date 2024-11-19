class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        node_set = set(nodes)

        def dfs(current):
            if not current:
                return None
            
            if current in node_set:
                return current
            
            left = dfs(current.left)
            right = dfs(current.right)

            if left and right:
                return current
            
            return left if left else right
        
        return dfs(root)
