class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        max_int = 2**31 - 1
        min_int = -2**31
        if divisor == 1:
            return dividend

        if dividend == min_int and divisor == -1:
            return max_int

        negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        for i in range(31, -1, -1):
            if (divisor << i) <= dividend:
                dividend -= divisor << i
                quotient += 1 << i

        return -quotient if negative else quotient
