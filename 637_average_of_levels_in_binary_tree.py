class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return 

        queue = deque([root])
        ans = []
        while queue:
            nodes_in_current_level = len(queue)
            level_sum = 0
            for _ in range(nodes_in_current_level):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(level_sum / nodes_in_current_level)

        return ans
