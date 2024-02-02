class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        counts = defaultdict(int)
        ans = []

        for num in arr:
            counts[num] += 1

        for key in counts:
            if key == counts[key]:
                ans.append(key)

        return -1 if not ans else max(ans)
