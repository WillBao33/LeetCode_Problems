class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == '1'

        def dfs(row, col):
            for dx, dy in direction:
                next_row, next_col = row + dy, col + dx
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    dfs(next_row, next_col)

        ans = 0
        seen = set()
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in seen:
                    ans += 1
                    seen.add((i,j))
                    dfs(i, j)

        return ans
