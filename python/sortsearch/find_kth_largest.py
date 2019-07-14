import operator
import random
# find the kth largest value in an unsorted array

# the solution is to use the quick sort-like strategy.
# generate a random pivot index, partition the array
# into two parts, one is less than value at pivot index,
# one is larger than the value at pivot index. if the
# number of larger part is k - 1, then the value at
# pivot index is the kth largest we want.

# time complexity is O(n), the worst time complexity
# could be O(n^2).

def find_kth_largest(array, k):
    def find_kth(comp):
        def partition_around_pivot(left, right, pivot_idx):
            pivot_value = array[pivot_idx]
            new_pivot_idx = left
            array[right], array[pivot_idx] = (array[pivot_idx],
                    array[right])
            for i in range(left, right):
                if comp(array[i], pivot_value):
                    array[i], array[new_pivot_idx] = (
                            array[new_pivot_idx], array[i])
                    new_pivot_idx += 1

            array[right], array[new_pivot_idx] = (
                    array[new_pivot_idx], array[right])

            return new_pivot_idx

        left, right = 0, len(array) - 1

        while left <= right:
            pivot_idx = random.randint(left, right)
            new_pivot_idx = partition_around_pivot(
                    left, right, pivot_idx)
            if new_pivot_idx == k - 1:
                return array[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:
                left = new_pivot_idx + 1

        return -1

    return find_kth(operator.gt)
