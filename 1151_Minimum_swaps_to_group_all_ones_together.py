class Solution:
    def minSwaps(self, data: List[int]) -> int:
        total_ones = sum(data)

        curr_ones = 0
        max_ones = 0

        for i in range(total_ones):
            curr_ones += data[i]
        max_ones = curr_ones
        for i in range(total_ones, len(data)):
            curr_ones += data[i] - data[i - total_ones]
            max_ones = max(max_ones, curr_ones)

        return total_ones - max_ones
