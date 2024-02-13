class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 

        queue = deque([root])
        x = 0
        level = 0
        max_sum = float('-inf')
        while queue:
            nodes_in_current_level = len(queue)
            level += 1
            level_sum = 0
            for i in range(nodes_in_current_level):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level_sum > max_sum:
                max_sum = level_sum
                x = level

        return x
