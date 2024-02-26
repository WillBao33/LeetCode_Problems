class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(curr, start, remaining_k, remaining_n):
            if remaining_k == 0 and remaining_n == 0:
                ans.append(curr[:])
                return 
            elif remaining_k == 0 or remaining_n <= 0:
                return 

            for i in range(start, 10):
                curr.append(i)
                backtrack(curr, i + 1, remaining_k - 1, remaining_n - i)
                curr.pop()

        ans = []
        backtrack([], 1, k, n)
        return ans
