# two pointers
class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        num = [i for i in str(abs(x))]
        i = 0
        j = len(num) - 1

        while i < j:
            num[i], num[j] = num[j], num[i]
            i += 1
            j -= 1
        if negative:
            num = -int(''.join(num))
        else:
            num = int(''.join(num))
        return 0 if num < -2**31 or num > 2**31 - 1 else num
