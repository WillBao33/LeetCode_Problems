class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if set(word1) != set(word2):
            return False

        counter1 = Counter(word1)
        counter2 = Counter(word2)

        if sorted(counter1.values()) != sorted(counter2.values()):
            return False

        return True
