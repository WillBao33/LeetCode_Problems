class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(nums[i]+prefix[-1])

        def binary_search(arr, target):
            left = 0
            right = len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return left

        
        ans = []
        for query in queries:
            i = binary_search(prefix, query)
            ans.append(i)
        return ans
