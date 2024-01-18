class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        int_max = 2**31 - 1
        int_min = -2**32

        i = 0
        negative = 0
        n = len(s)
        result = 0

        while i < n and s[i] == ' ':
            i += 1

        while i < n and s[i] in ['+','-']:
            negative = s[i] == '-'
            i += 1
            if i < n and s[i] in ['+','-']:
                return 0

        while i < n and s[i].isdigit():
            result = result*10 + int(s[i])
            i += 1

            if not negative and result >= int_max:
                return int_max
            if negative and result > int_max:
                return int_min

        return -result if negative else result
