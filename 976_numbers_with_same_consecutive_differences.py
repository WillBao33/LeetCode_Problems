class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def backtrack(curr, last_digit, remaining):
            if remaining == 0:
                ans.append(int(''.join(map(str, curr))))
                return 

            for next_digit in range(10):
                if abs(next_digit - last_digit) == k:
                    curr.append(next_digit)
                    backtrack(curr, next_digit, remaining - 1)
                    curr.pop()


        ans = []
        for first_digit in range(1, 10):
            backtrack([first_digit], first_digit, n - 1)

        return ans
