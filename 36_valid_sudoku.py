class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range (n)]

        for i in range(n):
            for j in range(n):
                val = board[i][j]
                if val == '.':
                    continue
                if val in rows[i]:
                    return False
                rows[i].add(val)

                if val in cols[j]:
                    return False
                cols[j].add(val)

                ix = (i//3)*3+j//3
                if val in boxes[ix]:
                    return False
                boxes[ix].add(val)

        return True
