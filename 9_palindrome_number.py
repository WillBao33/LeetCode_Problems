class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return 0

        value = int(str(x)[::-1])
        if x == value:
            return True
        else:
            return False
