class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        i = 0
        for num in asteroids:
            while stack and num < 0 < stack[-1]:
                if stack[-1] == -num:
                    stack.pop()
                    break
                elif stack[-1] < -num:
                    stack.pop()
                    continue
                elif stack[-1] > num:
                    break
            else:
                stack.append(num)

        return stack
