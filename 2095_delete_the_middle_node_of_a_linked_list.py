class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head.next or not head:
            return None
        s = head
        f = head

        while f and f.next:
            prev = s
            s = s.next
            f = f.next.next

        prev.next = s.next

        return head
