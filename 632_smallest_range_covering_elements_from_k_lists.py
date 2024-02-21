class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        current_max = float('-inf')
        
        # Initialize the heap
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            current_max = max(current_max, nums[i][0])

        start, end = float('-inf'), float('inf')
        
        # Process the heap
        while min_heap:
            current_min, list_idx, element_idx = heapq.heappop(min_heap)
            
            # Update the range if smaller
            if current_max - current_min < end - start:
                start, end = current_min, current_max
                
            # Add the next element from the same list to the heap
            if element_idx + 1 < len(nums[list_idx]):
                next_element = nums[list_idx][element_idx + 1]
                heapq.heappush(min_heap, (next_element, list_idx, element_idx + 1))
                current_max = max(current_max, next_element)
            else:
                # One of the lists is exhausted, break the loop
                break

        return [start, end]
