class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        start, maxLength = 0, 0
        for i in range(len(s)):
            len1 = expandAroundCenter(i, i)      # Odd length palindrome
            len2 = expandAroundCenter(i, i + 1)  # Even length palindrome
            length = max(len1, len2)

            if length > maxLength:
                maxLength = length
                start = i - (length - 1) // 2

        return s[start:start + maxLength]
