class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            # If the current permutation is complete
            if start == len(nums):
                ans.append(nums[:])
                return
            
            # Set to track duplicates in the current recursion level
            seen = set()
            for i in range(start, len(nums)):
                # Skip duplicate numbers to prevent duplicate permutations 
                # if two duplicates in a row, the first one already constructs all permutations that the second one can construct, so skip
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                
                # Swap the current element with the start element
                nums[start], nums[i] = nums[i], nums[start]
                
                # Recurse on the next element
                backtrack(start + 1)
                
                # Backtrack: swap back the elements
                nums[start], nums[i] = nums[i], nums[start]
        
        ans = []
        backtrack(0)
        return ans
