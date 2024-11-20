class Solution:
    def minimumKeypresses(self, s: str) -> int:
        freq = Counter(s)
        i , presses, output = 0, 1, 0

        for charj, num in freq.most_common():
            output += num * presses
            i += 1
            if i == 9:
                presses += 1
                i = 0

        return output