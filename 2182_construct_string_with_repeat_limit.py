from collections import Counter
import heapq
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        char_freq = Counter(s)

        max_heap = [(-ord(char),char) for char in char_freq]
        heapq.heapify(max_heap)

        result = []
        prev_char = None
        prev_count = 0
        while max_heap:
            _, char = heapq.heappop(max_heap)
            char_count = min(repeatLimit, char_freq[char])

            if prev_char and prev_char == char and prev_count == repeatLimit:
                if not max_heap:
                    break

                _, next_char = heapq.heappop(max_heap)
                result.append(next_char)
                char_freq[next_char] -= 1
                if char_freq[next_char] > 0:
                    heapq.heappush(max_heap,(-ord(next_char),next_char))

                prev_char = None
                prev_count = 0
                if char_freq[char] > 0:
                    heapq.heappush(max_heap,(-ord(char),char))

            else:
                result.extend([char]*char_count)
                char_freq[char] -= char_count
                prev_char = char
                prev_count = char_count

                if char_freq[char] > 0:
                    heapq.heappush(max_heap, (-ord(char),char))

        return "".join(result)
