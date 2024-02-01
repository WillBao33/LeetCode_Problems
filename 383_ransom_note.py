class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counts = defaultdict(int)
        for char in magazine:
            counts[char] += 1

        for char in ransomNote:
            if counts[char] > 0:
                counts[char] -= 1
            else:
                return False

        return True
