import collections
# given a sorted array of disjoint closed intervals,
# and an interval to be added, return the new union
# of these two.

# the solution breaks into three parts:
# 1. add all intervals that appear completely before
# the added interval
# 2. if the interval in the array intersects with
# the added interval, union into a new interval and
# repeat this step
# 3. add all remaining intervals that do not intersect
# with the added interval

# time complexity is O(n) where the n is the length
# of original sorted array.

Interval = collections.namedtuple('Interval', ('left', 'right'))

def add_interval(disjoint_intervals, new_interval):
    i, result = 0, []

    while (i < len(disjoint_intervals) and new_interval.left
            > disjoint_intervals[i].right):
        result.append(disjoint_intervals[i])
        i += 1

    while (i < len(disjoint_intervals) and new_interval.right
            >= disjoint_intervals[i].left):
        new_interval = Interval(
                min(disjoint_intervals[i].left, new_interval.left),
                max(disjoint_intervals[i].right, new_interval.right)
                )
        i += 1

    return result + [new_interval] + disjoint_intervals[i:]
