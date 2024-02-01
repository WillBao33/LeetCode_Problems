class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        counts = defaultdict(int)
        ans = len(cards) + 1

        for i, num in enumerate(cards):
            if num in counts:
                dist = i - counts[num] + 1
                ans = min(ans,dist)
            
            counts[num] = i

        return -1 if ans == len(cards) + 1 else ans
