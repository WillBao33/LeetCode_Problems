class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s, t = Counter(s), Counter(t)
        if s == t:
            return True

        return False
