class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return None
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        ans = []
        nums1 = Counter(nums1)
        for num in nums2:
            if num in nums1 and nums1[num] > 0:
                ans.append(num)
                nums1[num] -= 1

        return ans
