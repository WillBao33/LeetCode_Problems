from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)
        ordered = sorted(counts.values(), reverse = True)

        ans = 0
        size = 0
        n = len(arr)/2.0
        for freq in ordered:
            ans += 1
            size += freq
            if size >= n:
                return ans 
