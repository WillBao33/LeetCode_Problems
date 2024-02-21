from heapq import heapify, heappop, heappush
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        unused_rooms, used_rooms = list(range(n)), []
        heapify(unused_rooms)
        meeting_counts = [0] * n

        for start, end in sorted(meetings):
            while used_rooms and used_rooms[0][0] <= start:
                _, room = heappop(used_rooms)
                heappush(unused_rooms, room)
            if unused_rooms:
                room = heappop(unused_rooms)
                heappush(used_rooms,[end, room])
            else:
                room_avail_time, room = heappop(used_rooms)
                heappush(used_rooms, [room_avail_time + end - start, room])

            meeting_counts[room] += 1

        return meeting_counts.index(max(meeting_counts))
