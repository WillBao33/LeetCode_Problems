class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        char_list = list(s)


        left = 0 
        right = len(char_list) - 1
        while left < right:
            if char_list[left].isalpha() and char_list[right].isalpha():
                char_list[left], char_list[right] = char_list[right], char_list[left]
                left += 1
                right -= 1
            else:
                if char_list[left].isalpha() == False:
                    left += 1
                if char_list[right].isalpha() == False:
                    right -= 1

        return ''.join(char_list)
