class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 1

        def dfs(row, col):
            for dx, dy in direction:
                next_row, next_col = row + dy, col + dx
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    dfs(next_row, next_col)

        seen = set()
        direction = [(0,1), (1,0), (0,-1), (-1,0)]
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in [0, n - 1]:
                if grid[i][j] == 1 and (i,j) not in seen:
                    seen.add((i, j))
                    dfs(i, j)

        for j in range(n):
            for i in [0, m - 1]:
                if grid[i][j] == 1 and (i, j) not in seen:
                    seen.add((i,j))
                    dfs(i, j)
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in seen:
                    ans += 1

        return ans
