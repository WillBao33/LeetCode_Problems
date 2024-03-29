class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        x = abs(x)
        result = 0

        while x:
            digit = x % 10
            x //= 10
            result = result*10 + digit

        if negative:
            result = -result

        return result if -2**31 <= result <= 2**31 -1 else 0
