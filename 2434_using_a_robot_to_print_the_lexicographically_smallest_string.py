class Solution(object):
    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """
        min_right = ['z']*len(s)
        min_character = 'z'
        for idx in range(len(s)-1, -1, -1):
            min_right[idx] = min_character
            min_character = min(min_character, s[idx])
        
        res = []
        stack = []
        for idx, c in enumerate(s):
            stack.append(c)
            while stack and ord(stack[-1]) <= ord(min_right[idx]): # note: this will keep running until the top of the stack > min_right[idx]
                res.append(stack.pop())

            
        return "".join(res)
