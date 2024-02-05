class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s = head
        f = head 
        
        while f and f.next:
            s = s.next
            f = f.next.next

        return s
