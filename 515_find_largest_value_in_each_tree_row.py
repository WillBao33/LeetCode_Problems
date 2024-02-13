class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return 

        queue = deque([root])
        ans = []
        while queue:
            current_length = len(queue)
            level_max = float('-inf')

            for _ in range(current_length):
                node = queue.popleft()
                level_max = max(level_max,node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level_max)

        return ans
