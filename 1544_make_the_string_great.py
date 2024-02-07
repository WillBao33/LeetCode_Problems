class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for c in s:
            if stack and (stack[-1].islower() and c == stack[-1].upper() or stack[-1].isupper() and c == stack[-1].lower()):
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)
