class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 
        queue = deque([root])
        while queue:
            nodes_in_current_level = len(queue)
            leaves_sum = 0

            for _ in range(nodes_in_current_level):
                node = queue.popleft()
                leaves_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return leaves_sum
