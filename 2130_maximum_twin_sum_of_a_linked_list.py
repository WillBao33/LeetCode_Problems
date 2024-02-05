class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        length = 0 
        dummy = head

        while dummy:
            length += 1
            dummy = dummy.next

        s = head
        for _ in range(length // 2):
            s = s.next

        prev = None
        curr = s
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        n_s = prev
        n_f = head
        max_sum = 0
        for _ in range(length // 2):
            twin_sum = n_s.val + n_f.val
            max_sum = max(max_sum, twin_sum)
            n_f = n_f.next
            n_s = n_s.next

        return max_sum
