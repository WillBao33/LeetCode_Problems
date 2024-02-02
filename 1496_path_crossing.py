class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        visited = set()
        curr = (0,0)
        visited.add(curr)
        for dirc in path:
            x, y = curr
            if dirc == 'N':
                curr = (x,y+1)
            elif dirc == 'S':
                curr = (x,y-1)
            elif dirc == 'E':
                curr = (x+1,y)
            elif dirc == 'W':
                curr = (x-1,y)
            
            if curr in visited:
                return True
            
            visited.add(curr)
        return False
