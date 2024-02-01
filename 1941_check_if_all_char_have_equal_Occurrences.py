from collections import defaultdict
class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        counts = defaultdict(int)

        for c in s:
            counts[c] += 1

        frequencies = counts.values()

        return len(set(frequencies)) == 1
        
