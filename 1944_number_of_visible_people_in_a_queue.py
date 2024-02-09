class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        stack = deque()
        answer = [0]*len(heights)

        for i, height in enumerate(heights):
            while stack and height > heights[stack[-1]]:
                answer[stack[-1]] += 1
                stack.pop()
            if stack:
                answer[stack[-1]] += 1

            stack.append(i)

        return answer
