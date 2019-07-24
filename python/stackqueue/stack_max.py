# implement a stack class with max API, the max method should have O(1)
# time complexity.

class Stack(object):
    class MaxWithCount(object):
        def __init__(self, max_value, count):
            self.max = max_value
            self.count = count

    def __init__(self):
        self._element = []
        self._max = []

    def empty(self):
        return len(self._element) == 0

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._max[-1].max

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        res = self._element.pop()
        if res == self._max[-1].max:
            self._max[-1].count -= 1
            if self._max[-1].count == 0:
                self._max.pop()

        return res

    def push(self, value):
        if self.empty() or value > self._max[-1].max:
            self._max.append(MaxWithCount(value, 1))
        elif value == self._max[-1].max:
            self._max[-1].count += 1

        self._element.append(value)
