class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        max_length = 0
        char_map = {}

        for end in range(0,len(s)):
            current_char = s[end]

            if current_char in char_map:
                start = max(start,char_map[current_char] + 1)

            char_map[current_char] = end
            max_length = max(max_length, end - start + 1)

        return max_length

        
