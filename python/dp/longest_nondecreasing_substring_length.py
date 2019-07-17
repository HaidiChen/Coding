# compute the length of longest nondecreasing substring in
# a given unsorted integer array.

# the solution is to calculate the length of longest substring
# that ends at each index i and then return the maximum one.
# so the length of longest substring ending at index i equals:
# length[i] = 1 (as array[i] is less than every entry before it)
# or
# length[i] = 1 + max(length[0],...,length[i-1]) if array[i] >=
# array[j] where 0 <= j < i

# the time complexity is O(n^2)
# the space complexity is O(n)

class Solution:
    def longest_nondecreasing_substring_length(self, array):
        length = [1] * len(array)

        for i in range(1, len(array)):
            length[i] = max(1 + max([length[j] for j in range(i)
                if array[i] >= array[j]], default=0), length[i])

        return max(length)
