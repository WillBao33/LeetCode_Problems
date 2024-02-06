class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        if not head.next:
            return head.val

        dummy = ListNode(0)
        dummy.next = head
        length = 0
        value = 0
        current = head
        while current:
            length += 1
            current = current.next

        for i in range(length,-1,-1):
            value += (dummy.val) * 2**i
            dummy = dummy.next

        return value
