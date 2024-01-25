class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        The following way is the brute-force method. It does what the question asks but the efficiency is low.
        """
        max_area = 0 
        bar_num = len(height)-1
        if len(height) == 0 or len(height) == 1:
            return 0
        if len(height) == 2:
            return min(height)

        for i in reversed(range(len(height))):
            width = 1
            for j in reversed(range(bar_num)):
                area = min(height[i],height[j])*width
                width += 1
                if area >= max_area:
                    max_area = area
            bar_num -= 1

        return max_area
