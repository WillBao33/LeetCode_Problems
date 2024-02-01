class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        counts = defaultdict(int)
        ans = [[],[]]

        for match in matches:
            counts[match[0]] += 0
            counts[match[1]] += 1
        for key in counts:
            if counts[key] == 0:
                ans[0].append(key)
            elif counts[key] == 1:
                ans[1].append(key)
        ans[0].sort()
        ans[1].sort()

        return ans
