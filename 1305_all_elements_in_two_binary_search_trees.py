class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def inorderTraversal(root, sortedList):
            if not root:
                return

            inorderTraversal(root.left, sortedList)
            sortedList.append(root.val)
            inorderTraversal(root.right,sortedList)

        sorted_list1, sorted_list2 = [], []
        inorderTraversal(root1, sorted_list1)
        inorderTraversal(root2, sorted_list2)

        i, j = 0, 0
        merged_list = []
        while i <len(sorted_list1) and j < len(sorted_list2):
            if sorted_list1[i] < sorted_list2[j]:
                merged_list.append(sorted_list1[i])
                i+=1
            else:
                merged_list.append(sorted_list2[j])
                j+=1

        merged_list.extend(sorted_list1[i:])
        merged_list.extend(sorted_list2[j:])

        return merged_list
