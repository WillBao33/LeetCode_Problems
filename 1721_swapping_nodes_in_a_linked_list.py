class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        k_from_start = head
        for _ in range(k - 1):
            k_from_start = k_from_start.next

        k_from_end = head
        for _ in range(length - k):
            k_from_end = k_from_end.next
        
        k_from_start.val, k_from_end.val = k_from_end.val, k_from_start.val



        return head
