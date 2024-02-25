class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(mid):
            curr_sum = 0
            splits = 0
            for num in nums:
                if curr_sum + num <= mid:
                    curr_sum += num
                else:
                    splits += 1
                    curr_sum = num

            return splits + 1

        left = max(nums)
        right = sum(nums)
        while left <= right:
            mid = (left + right) // 2
            if check(mid) <= k:
                right = mid - 1
                ans = mid
            else:
                left = mid + 1

        return ans
