class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.left and not root.right:
                root = root.left
            elif root.right and not root.left:
                root = root.right
            else:
                temp = self.findMin(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right, root.val)
                
        return root
    
    def findMin(self, node):
        while node.left:
            node = node.left
        return node
