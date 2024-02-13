class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 

        queue = deque([root])
        even = True
        while queue:
            level_len = len(queue)
            if even:
                prev_node = 0
            else:
                prev_node = float('inf')
            for _ in range(level_len):
                node = queue.popleft()
                if even:
                    if node.val % 2 == 0 or node.val <= prev_node:
                        return False
                else:
                    if node.val % 2 != 0 or node.val >= prev_node:
                        return False

                prev_node = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            even = not even

        return True
