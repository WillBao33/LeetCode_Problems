class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = defaultdict(list)
        ans = -1
        def digitSum(n):
            return sum(int(digit) for digit in str(n))

        for num in nums:
            sums = digitSum(num)
            counts[sums].append(num)
            counts[sums].sort(reverse=True)

        for arr in counts.values():
            if len(arr) >= 2:
                ans = max(ans,arr[0]+arr[1])
            
        return ans
