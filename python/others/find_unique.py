# given a list of numbers, where every number shows up twice except for one
# number, find that one number

# the solution is to use dictionary to count all the numbers and then iterate
# through the dictionary to find the count that is one.
# time complexity of this approach is O(n)
# space complexity is also O(n)

# an alternative solution is to XOR all the numbers and the result is going to
# be the unique number. Why? because two same numbers doing an XOR operation
# returns 0, and 0 XOR with any number, say k, is not going to change anything,
# so 0 ^ k = k. after we XORed every number in the array, it finally turns to
# 0 ^ k where the k is that unique number we want.
# time complexity of this solution is also O(n)
# space complexity is, however, O(1)

class Solution(object):
    """
    """
    def find_unique(self, array):
        counters = {}

        for e in array:
            if e not in counters:
                counters[e] = 1
            else:
                counters[e] += 1

        for key in counters:
            if counters[key] == 1:
                return key

        return -1

    def find_unique2(self, array):
        result = array[0]
        for n in array[1:]:
            result ^= n

        return result
