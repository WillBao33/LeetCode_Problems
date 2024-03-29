class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(char.lower() for char in s if char.isalnum())
        i = 0
        j = len(string) - 1
        while i < j:
            if string[i] == string[j]:
                i += 1
                j -= 1
            else:
                return False

        return True
