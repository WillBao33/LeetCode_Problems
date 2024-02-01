class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 0
        unique_set = set(arr)
        for n in arr:
            if n+1 in unique_set:
                count += 1
                
        return count
