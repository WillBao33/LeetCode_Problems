class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        counts = defaultdict(int)

        for num in arr:
            counts[num] += 1

        my_set = set(counts.values())

        return len(counts) == len(my_set)
