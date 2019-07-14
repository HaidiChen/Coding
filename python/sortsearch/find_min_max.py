import collections
# find the min and max simultaneously in an unsorted array.

# compare pairs at a time. e.g., array is [3,2,5,1,2,4],
# first compare 3 and 2, since 3 > 2, set max to be 3 and min
# to be 2; then compare 5 and 1, since 5 > 1, 5 is a candidate
# for the max, compare 5 with current max which is 3, 5 > 3,
# so update max to be 5, same goes to the min, 1 < 2, update
# min to be 1; then compare 2 and 4, 4 > 2, but 4 < 5 and 2 > 1
# so min and max are not updated. Also, if the length of array
# is odd, we need to compare the last value with both current
# max and min value.

# time complexity is O(n)

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))

def find_min_max(array):
    def min_max(a, b):
        return MinMax(a, b) if a < b else MinMax(b, a)

    if len(array) <= 1:
        return MinMax(array[0], array[0])

    global_min_max = min_max(array[0], array[1])

    for i in range(2, len(array) - 1, 2):
        local_min_max = min_max(array[i], array[i + 1])
        global_min_max = MinMax(
                min(global_min_max.smallest, local_min_max.smallest),
                max(global_min_max.largest, local_min_max.largest))


    if len(array) % 2:
        global_min_max = MinMax(
                min(global_min_max.smallest, array[-1]),
                max(global_min_max.largest, array[-1]))

    return global_min_max
