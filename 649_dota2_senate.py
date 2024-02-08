class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        n = len(senate)
        r_queue = deque()
        d_queue = deque()

        for i, s in enumerate(senate):
            if s == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)

        while r_queue and d_queue:
            r_idx, d_idx = r_queue.popleft(), d_queue.popleft()
            if r_idx < d_idx:
                r_queue.append(n+r_idx)
            else:
                d_queue.append(n+d_idx)

        return "Radiant" if r_queue else "Dire"
