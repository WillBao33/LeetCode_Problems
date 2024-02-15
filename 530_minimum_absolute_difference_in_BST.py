class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def iterative_inorder(node):
            if not node:
                return 
            stack = []
            curr = root
            values = []
            while stack or curr:
                if curr:
                    stack.append(curr)
                    curr = curr.left
                else:
                    curr = stack.pop()
                    values.append(curr.val)
                    curr = curr.right

            return values
        
        values = iterative_inorder(root)
        ans = float('inf')
        for i in range(1,len(values)):
            ans = min(ans, abs(values[i]-values[i-1]))

        return ans
        # def dfs(node):
        #     if not node:
        #         return

        #     left = dfs(node.left)
        #     values.append(node.val)
        #     right = dfs(node.right)

        # values = []
        # dfs(root)
        # ans = float('inf')
        # for i in range(1, len(values)):
        #     ans = min(ans, abs(values[i]-values[i-1]))

        # return ans
