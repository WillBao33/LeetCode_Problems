'''
Basically using the binary search algorithm on the shorter array. Creating partitions in both array and compare both values of left max side to both values of right min side in a crossed direction.
'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2

        start, end = 0, m

        while start <= end:
            mid1 = (start + end) // 2
            mid2 = half - mid1

            leftMax1 = float('-inf') if mid1 == 0 else nums1[mid1 - 1]
            leftMax2 = float('-inf') if mid2 == 0 else nums2[mid2 - 1]

            rightMin1 = float('inf') if mid1 == m else nums1[mid1]
            rightMin2 = float('inf') if mid2 == n else nums2[mid2]

            if leftMax1 <= rightMin2 and leftMax2 <= rightMin1:
                if total % 2 == 0:
                    return (max(leftMax1, leftMax2) + min(rightMin1, rightMin2)) / 2.0
                else:
                    return max(leftMax1, leftMax2)
                
            elif leftMax1 > rightMin2:
                end = mid1 - 1
            else:
                start = mid1 + 1


