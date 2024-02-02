class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counts = defaultdict(int)

        for char in s:
            counts[char] += 1

        sorted_counts = sorted(counts.items(),key = lambda item:item[1], reverse=True)

        return ''.join(item[0]*item[1] for item in sorted_counts)
