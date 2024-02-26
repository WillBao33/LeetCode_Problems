class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(curr, openN, closeN):
            if len(curr) == 2*n:
                ans.append(curr)
                return 

            if openN < n:
                backtrack(curr +'(', openN + 1, closeN)
            
            if closeN < openN:
                backtrack(curr + ')', openN, closeN + 1)

        
        ans = []
        backtrack('', 0, 0)
        return ans
