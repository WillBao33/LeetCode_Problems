class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = defaultdict(list)
        for i, mgr in enumerate(manager):
            if manager[i] >= 0:
                subordinates[mgr].append(i)

        def dfs(empID, totalTime):
            if not subordinates[empID]:
                return totalTime
            maxTime = 0
            for sub in subordinates[empID]:
                maxTime = max(maxTime, dfs(sub, totalTime + informTime[empID]))

            return maxTime

        return dfs(headID, 0)
