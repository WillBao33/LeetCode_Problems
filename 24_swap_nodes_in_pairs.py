class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
            
        dummy = head.next
        prev = None

        while head and head.next:
            if prev:
                prev.next = head.next
            prev = head

            nextNode = head.next.next 
            head.next.next = head

            head.next = nextNode
            head = nextNode

        return dummy
