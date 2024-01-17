class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = x < 0
        x = abs(x)
        reversed_num = 0

        max = 2**31 - 1

        while x != 0:
            digit = x % 10
            x = x // 10

            if reversed_num > max // 10 or (reversed_num == max // 10 and digit > max % 10):
                return 0

            reversed_num = reversed_num*10+digit

        return -reversed_num if negative else reversed_num
