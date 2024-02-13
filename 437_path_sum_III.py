class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0

        def dfs(node, currSumPath):
            if not node:
                return 

            currSumPath = [x + node.val for x in currSumPath] + [node.val]

            self.count += currSumPath.count(targetSum)

            dfs(node.left,currSumPath)
            dfs(node.right,currSumPath)
        
        dfs(root, [])
        return self.count
