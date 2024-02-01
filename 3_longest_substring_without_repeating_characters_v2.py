class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        counts = defaultdict(int)
        ans = 0
        start = 0 

        for i, char in enumerate(s):
            if char in counts and counts[char] >= start:
                start = counts[char] + 1
            else: 
                ans = max(ans, i - start + 1)

            counts[char] = i

        return ans
