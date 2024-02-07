class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        matching = {"(":")", "[":"]", "{":"}"}
        most_recent = ""

        for char in s:
            if char in matching:
                most_recent = char
                stack.append(char)
            else:
                if not stack:
                    return False
                most_recent = stack[-1]
                if char == matching[most_recent]:
                    stack.pop()
                else:
                    return False

        return not stack
            
