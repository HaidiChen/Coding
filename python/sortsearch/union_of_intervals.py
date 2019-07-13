import collections

# compute the union of intervals

# time complexity is dominated by the sorting(i.e., O(nlogn))

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

class Interval:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __lt__(self, other):
        if self.left.val != other.left.val:
            return self.left.val < other.left.val
        return self.left.is_closed and not other.left.is_closed


def union_of_intervals(intervals):
    if not intervals:
        return []

    intervals.sort()
    result = [intervals[0]]
    for i in intervals:
        if intervals and (i.left.val < result[-1].right.val or
                (i.left.val == result[-1].right.val and
                    (i.left.is_closed or result[-1].right.is_closed))):
                    if (i.right.val > result[-1].right.val or
                            (i.right.val == result[-1].right.val and 
                                i.right.is_closed)):
                                result[-1].right = i.right
        else:
            result.append(i)

    return result
