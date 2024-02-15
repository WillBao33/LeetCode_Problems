class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 1
        
        def dfs(row, col):
            curr_area = 1
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    curr_area += dfs(next_row, next_col)
            return curr_area
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        seen = set()
        ans = 0
        m = len(grid)
        n = len(grid[0])
        max_area = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row, col) not in seen:
                    seen.add((row, col))
                    max_area = max(max_area,dfs(row, col))
                    
        
        return max_area
