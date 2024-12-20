class Solution:
    def makePalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        operations = 0

        while left < right:
            if s[left] != s[right]:
                operations += 1
                if operations > 2:
                    return False

            left += 1
            right -= 1

        return operations <= 2