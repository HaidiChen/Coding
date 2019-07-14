import collections
import functools

# given an array which has element from 0 ~ n - 1, the length
# of this array is n and there's one element appearing twice
# and one element is missing. find the missing and duplicate.

# time complexity is O(n)
# space complexity is O(1)

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
        ('duplicate', 'missing'))

def find_duplicate_missing(array):
    miss_XOR_dup = functools.reduce(lambda v, i: v ^ i[0] ^ i[1],
            enumerate(array), 0)

    differ_bit, miss_or_dup = miss_XOR_dup & (~(miss_XOR_dup - 1)), 0
    for i, a in enumerate(array):
        if i & differ_bit:
            miss_or_dup ^= i
        if a & differ_bit:
            miss_or_dup ^= a

    if miss_or_dup in array:
        return DuplicateAndMissing(miss_or_dup, miss_or_dup ^
                miss_XOR_dup)

    return DuplicateAndMissing(miss_or_dup ^ miss_XOR_dup, miss_or_dup)
