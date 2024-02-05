class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == right:
            return head
        
        dummy = ListNode(0,head)
        prev_left = dummy

        for _ in range(left - 1):
            prev_left = prev_left.next

        curr = prev_left.next
        prev = None

        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        prev_left.next.next = curr
        prev_left.next = prev


        return dummy.next
