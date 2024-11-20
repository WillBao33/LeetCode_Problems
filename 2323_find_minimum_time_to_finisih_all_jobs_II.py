import math

class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        return max(math.ceil(job / worker) for job, worker in zip(sorted(jobs), sorted(workers)))