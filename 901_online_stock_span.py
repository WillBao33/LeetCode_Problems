class StockSpanner(object):

    def __init__(self):
        self.queue = deque()
    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span = 1
        while self.queue and self.queue[-1][0] <= price:
            _, s = self.queue.pop()
            span += s
        self.queue.append((price,span))
        return span
