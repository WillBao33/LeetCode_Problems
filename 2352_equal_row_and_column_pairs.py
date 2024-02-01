class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def convert_to_key(arr):
            return tuple(arr)

        dic = defaultdict(int)
        for row in grid:
            dic[convert_to_key(row)] += 1

        dic2 = defaultdict(int)
        for col in range(len(grid[0])):
            current_col = []
            for row in range(len(grid)):
                current_col.append(grid[row][col])

            dic2[convert_to_key(current_col)] += 1

        ans = 0
        for key in dic:
            ans += dic[key] * dic2[key]

        return ans
