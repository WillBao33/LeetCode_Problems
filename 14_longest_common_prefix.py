class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        i = 0
        if not strs:
            return ""

        min_length = min(len(s) for s in strs)

        while i < min_length:
            letter = strs[0][i]
            if  all(s[i] == letter for s in strs):
                prefix += letter
                i += 1
            else:
                break

        return prefix
