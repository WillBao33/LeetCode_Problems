from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        frequencies = Counter(arr)
        ordered = sorted(frequencies.values(), reverse = True)
        while k:
            val = ordered[-1]
            if val <= k:
                k -= val
                ordered.pop()

            else:
                break

        return len(ordered)
