# implement a queue with max API
import collections

class Queue(object):
    def __init__(self):
        self._entries = collections.deque()
        self._max = collections.deque()

    def enqueue(self, x):
        self._entries.append(x)

        while self._max and self._max[-1] < x:
            self._max.pop()
        self._max.append(x)

    def dequeue(self):
        if self._entries:
            result = self._entries.popleft()
            if result == self._max[0]:
                self._max.popleft()
            return result

        raise IndexError('empty queue')

    def max(self):
        if self._max:
            return self._max[0]

        raise IndexError('empty queue')
