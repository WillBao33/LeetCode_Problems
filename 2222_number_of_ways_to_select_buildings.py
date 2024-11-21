class Solution:
    def numberOfWays(self, s: str) -> int:
        valid_ways = 0
        zero = one = zero_one = one_zero = 0

        for c in s:
            if c == "0":
                zero += 1
                one_zero += one
                valid_ways += zero_one
            else:
                one += 1
                zero_one += zero
                valid_ways += one_zero
        return valid_ways