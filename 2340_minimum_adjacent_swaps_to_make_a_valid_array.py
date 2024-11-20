class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        index_smallest, index_largest = 0, 0
        n = len(nums)

        for i in range(n):
            if nums[i] < nums[index_smallest]:
                index_smallest = i
            if nums[i] >= nums[index_largest]:
                index_largest = i

        swaps = index_smallest + (n - 1 - index_largest)

        if index_smallest > index_largest:
            swaps -= 1

        return swaps