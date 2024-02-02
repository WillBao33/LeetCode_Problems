class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        if len(pattern) != len(s.split()):
            return False

        p_dict = {}
        s_dict = {}

        for p_item, s_item in zip(list(pattern),s.split()):
            if p_item in p_dict:
                if p_dict[p_item] != s_item:
                    return False
            else:
                p_dict[p_item] = s_item

            if s_item in s_dict:
                if s_dict[s_item] != p_item:
                    return False
            else:
                s_dict[s_item] = p_item

        return True
