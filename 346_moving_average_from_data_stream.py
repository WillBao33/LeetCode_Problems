class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.size = size
        self.queue = []

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        total = float(sum(self.queue[-self.size:]))

        return total / min(len(self.queue),self.size)
