import heapq
class SeatManager:

    def __init__(self, n: int):
        self.heap = list(range(1,n+1))
        heapq.heapify(self.heap)

    def reserve(self) -> int:
        seat = heapq.heappop(self.heap)
        return seat

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)
