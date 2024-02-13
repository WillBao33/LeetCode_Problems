class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return 
        queue = deque([root])
        ans = []
        while queue:
            nodes_in_current_level = len(queue)
            ans.append(queue[-1].val)

            for _ in range(nodes_in_current_level):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return ans
