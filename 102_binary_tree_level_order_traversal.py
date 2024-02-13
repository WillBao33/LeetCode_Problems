class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return 

        queue = deque([root])
        ans = []
        while queue:
            nodes_in_current_level = len(queue)
            level_list = []
            for _ in range(nodes_in_current_level):
                node = queue.popleft()
                level_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(level_list)

        return ans
