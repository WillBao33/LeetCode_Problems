class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        better solution
        """
        max_area = 0 
        left, right = 0, len(height) - 1

        while left < right:
            width = right - left
            current_area = width*min(height[left],height[right])
            max_area = max(max_area,current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
