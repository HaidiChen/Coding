# return the minimum and maximum value in a sequence
# using recursion instead of loop

class MinMax(object):
    def __init__(self, sequence):
        self.sequence = sequence

    def get_min(self):
        return self._get_helper(0, True)

    def get_max(self):
        return self._get_helper(0)

    def _get_helper(self, offset, is_min=False):
        if offset == len(self.sequence) - 1:
            return self.sequence[offset]
        if is_min:
            return min(self.sequence[offset], self._get_helper(offset + 1, True))

        return max(self.sequence[offset], self._get_helper(offset + 1))
