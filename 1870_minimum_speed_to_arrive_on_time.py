class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) > ceil(hour):
            return -1
        def check(speed):
            hours = 0
            for i in range(len(dist)):
                if i == len(dist) - 1:
                    hours += dist[i] / speed
                else:
                    hours += ceil(dist[i] / speed)

            return hours <= hour

        left = 1
        right = 10 ** 7
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
