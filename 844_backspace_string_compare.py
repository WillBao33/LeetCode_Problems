class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack1 = []
        stack2 = []

        for c in s:
            if c != "#":
                stack1.append(c)
            elif stack1:
                stack1.pop()

        for c in t:
            if c != "#":
                stack2.append(c)
            elif stack2:
                stack2.pop()

        return True if "".join(stack1) == "".join(stack2) else False
