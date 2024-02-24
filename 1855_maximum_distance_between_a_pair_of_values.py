class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        for i in range(len(nums1)):
            left, right = 0, len(nums2) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums1[i] <= nums2[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

            ans = max(ans, right - i)

        return ans
