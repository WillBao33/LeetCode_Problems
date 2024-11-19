class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        out = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candy:
                out.append(True)
            else:
                out.append(False)

        return out