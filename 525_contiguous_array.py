class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = ans = 0
        my_dict = defaultdict(int)
        my_dict[0] = -1
        
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            
            if count in my_dict:
                ans = max(ans,i - my_dict[count])
            else:
                my_dict[count] = i
                
        return ans
