class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        prefix = [gain[0]]
        for i in range(1,len(gain)):
            prefix.append(gain[i]+prefix[-1])

        return 0 if max(prefix) < 0 else max(prefix)
