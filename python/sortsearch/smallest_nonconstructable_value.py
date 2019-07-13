# given an input array (not sorted), find the smallest
# value that is not constructable using the values in
# this array

# e.g., A is <1,1,1,1,1,5,10,25>, the result should be
# 21 as you cannot build 21 through any combination.

# the solution is sorting the input first, and then
# calculate the sum of first k elements, compare it with
# the k + 1 element, if sum + 1 >= array[k+1], we continue
# to look at the next value, if not, we return the sum + 1
# as the result

# time complexity is dominated by sorting which is
# O(nlogn) where n is the length of array

def smallest_nonconstructable_value(array):
    sum = 0
    for e in sorted(array):
        if sum + 1 < e:
            return sum + 1
        sum += e

    return sum + 1
