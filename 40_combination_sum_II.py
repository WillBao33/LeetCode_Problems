class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(curr, start, target):
            if target == 0:
                ans.append(curr[:])
                return 

            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                curr.append(candidates[i])
                backtrack(curr, i + 1, target - candidates[i])
                curr.pop()

        ans = []
        backtrack([], 0, target)
        return ans
