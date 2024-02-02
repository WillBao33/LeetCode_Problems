class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        mst = {}
        mts = {}

        for char_s, char_t in zip(s,t):
            if char_s in mst:
                if mst[char_s] != char_t:
                    return False
            else:
                mst[char_s] = char_t

            if char_t in mts:
                if mts[char_t] != char_s:
                    return False
            else:
                mts[char_t] = char_s

        return True
