class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.current = 1
        self.exist = set()

    def popSmallest(self) -> int:
        if not self.heap:
            self.current += 1
            return self.current - 1
        else:
            smallest = heapq.heappop(self.heap)
            self.exist.remove(smallest)
            return smallest

    def addBack(self, num: int) -> None:
        if num >= self.current or num in self.exist:
            return 

        heapq.heappush(self.heap,num)
        self.exist.add(num)
