from bisect import bisect_left
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        # Dictionary to hold sorted lists of heights for each length
        length_to_heights = defaultdict(list)

        # Populate the dictionary
        for l, h in rectangles:
            length_to_heights[h].append(l)

        # Sort the height lists for each length
        for h in length_to_heights:
            length_to_heights[h].sort()

        def countForPoint(x, y):
            count = 0
            # Iterate through each length that is >= x
            for h in length_to_heights:
                if h >= y:
                    # Perform binary search to find the count of heights >= y
                    lengths = length_to_heights[h]
                    idx = bisect_left(lengths, x)
                    count += len(lengths) - idx  # Add the count of valid heights for this length
            return count

        # For each point, count the number of rectangles that can contain it
        return [countForPoint(x, y) for x, y in points]
