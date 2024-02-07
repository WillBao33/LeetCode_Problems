class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        splits = path.split("/")
        stack = []

        for item in splits:
            if item == "." or item == "":
                continue
            elif item == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(item)

        return "/"+"/".join(stack)
