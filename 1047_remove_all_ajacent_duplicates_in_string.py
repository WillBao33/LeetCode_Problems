class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s

        prev = ""
        stack = []
        for c in s:
            if c != prev:
                stack.append(c)
                prev = c
            else:
                stack.pop()
                if stack:
                    prev = stack[-1]
                else:
                    prev = ""

        return "".join(stack)
