class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        counts = defaultdict(int)
        
        for char in text:
            if char in 'balloon':
                counts[char] += 1
            
        counts['l'] //= 2
        counts['o'] //= 2
        
        return min(counts.get(char,0) for char in 'balloon')
