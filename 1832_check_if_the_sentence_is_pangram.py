class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        if len(sentence) < 26:
            return False
        
        alpha = set()
        for i in range(len(sentence)):
            if sentence[i] not in alpha:
                alpha.add(sentence[i])
                
        return True if len(alpha) >= 26 else False
