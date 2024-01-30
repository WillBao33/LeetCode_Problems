class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        reversed_words = []
        for word in words:
            char_list = list(word)
            left = 0
            right = len(char_list) - 1
            while left < right:
                char_list[left], char_list[right] = char_list[right], char_list[left]
                left += 1
                right -= 1

            reversed_words.append(''.join(char_list))

        return ' '.join(reversed_words)
