class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        @cache
        def dp(row, col):
            if row == m - 1:
                return matrix[row][col]
            
            path_sums = [dp(row + 1, col)]
            if col > 0:
                path_sums.append(dp(row + 1, col - 1))
            if col < n - 1:
                path_sums.append(dp(row + 1, col + 1))

            return matrix[row][col] + min(path_sums)

        m = len(matrix)
        n = len(matrix[0])

        return min(dp(0, col) for col in range(n))
