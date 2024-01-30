class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        i = j = 0
        current_cost = 0 
        max_length = 0 

        for j in range(len(s)):
            current_cost += abs(ord(s[j])-ord(t[j]))
            while current_cost > maxCost:
                current_cost -= abs(ord(s[i])-ord(t[i]))
                i += 1

            max_length = max(max_length, j - i + 1)

        return 0 if current_cost > maxCost else max_length
