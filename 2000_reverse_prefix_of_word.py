class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        char_list = list(word)
        if ch not in char_list:
            return word

        index = char_list.index(ch)

        i = 0
        while i < index:
            char_list[i], char_list[index] = char_list[index], char_list[i]
            i += 1
            index -= 1

        return ''.join(char_list)
