class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for i in range(len(s)):
            letter = s[i]
            if letter in dic:
                return letter
            dic[letter] = i

        return None
