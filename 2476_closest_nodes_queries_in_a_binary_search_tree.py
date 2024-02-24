# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        def dfs(root):
            def inorder(node, elements):
                if not node:
                    return 

                inorder(node.left, elements)
                elements.append(node.val)
                inorder(node.right, elements)

            elements = []
            inorder(root, elements)
            return elements

        def findMini(array, query):
            left, right = 0, len(array) - 1
            mini = -1
            while left<=right:
                mid = (left + right) // 2
                if array[mid] <= query:
                    mini = array[mid]
                    left = mid + 1
                else:
                    right = mid - 1
            return mini
        def findMaxi(array, query):
            left, right = 0, len(array) - 1
            maxi = -1
            while left<=right:
                mid = (left + right) // 2
                if array[mid] >= query:
                    maxi = array[mid]
                    right = mid - 1
                else:
                    left = mid + 1
            return maxi

        arr = dfs(root)
        ans = []
        for query in queries:
            mini = findMini(arr, query)
            maxi = findMaxi(arr, query)
            ans.append([mini,maxi])

        return ans
