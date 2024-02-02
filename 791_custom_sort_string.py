class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        s_count = Counter(s)

        result = []

        for char in order:
            if char in s_count:
                result.append(char*s_count[char])
                del s_count[char]
        for char, count in s_count.items():
            result.append(char*count)

        return ''.join(result)
