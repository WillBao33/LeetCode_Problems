class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        
        dummy = ListNode(0,head)
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        current = dummy 
        for _ in range(length - n):
            current = current.next

        current.next = current.next.next

        return dummy.next
