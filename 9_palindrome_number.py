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

# below is the way without converting to string
        if x < 0 or (x % 10 == 0 and x != 0):
            return 0

        reverse = 0 
        while x > reverse:
            reverse = reverse * 10 + x % 10 
            x = x // 10

        return x == reverse or x == reverse // 10
