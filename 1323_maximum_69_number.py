class Solution:
    def maximum69Number (self, num: int) -> int:
        for i, char in enumerate(str(num)):
            if char == '6':
                return int(str(num)[:i]+'9'+str(num)[i+1:])

        return num
