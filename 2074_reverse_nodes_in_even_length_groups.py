class Solution(object):
    def reverseEvenLengthGroups(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prevGroupEnd = dummy

        current = head
        groupLength = 1

        while current:
            count = 0
            groupIter = current

            while groupIter and count < groupLength:
                groupIter = groupIter.next
                count += 1

            if count % 2 == 0:
                newGroupEnd = current
                prev, curr = None, current
                for _ in range(count):
                    nextTemp = curr.next
                    curr.next = prev
                    prev, curr = curr, nextTemp

                prevGroupEnd.next = prev
                newGroupEnd.next = curr
                prevGroupEnd = newGroupEnd
            else:
                for _ in range(count):
                    prevGroupEnd = prevGroupEnd.next

            current = prevGroupEnd.next
            groupLength += 1

        return dummy.next
