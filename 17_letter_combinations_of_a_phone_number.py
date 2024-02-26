class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {
            '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'
        }

        def backtrack(index, path):
            if len(path) == len(digits):
                ans.append(''.join(path))
                return 

            for letter in phone[digits[index]]:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()


        ans = []
        backtrack(0,[])
        return ans
