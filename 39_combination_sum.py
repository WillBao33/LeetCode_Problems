class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(curr, start, target):
            if target == 0:
                ans.append(curr[:])
                return 

            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                curr.append(candidates[i])
                backtrack(curr, i, target - candidates[i])
                curr.pop()

        ans = []
        backtrack([], 0, target)
        return ans
