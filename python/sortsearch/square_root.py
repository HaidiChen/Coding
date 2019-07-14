# given a nonnegative integer, return the largest integer whose square
# is less than or equal to the given integer.

# the solution is to start with a range of 0 through k, compute the 
# middle value's square. if m^2 > k, the all subsequent values are
# greater than k, so we take the left half of range which is 0 through
# k/2. if m^2 <= k, then all previous values are less than or equal to
# the k, we take the right. when the range is empty, return the left
# endpoint - 1 as the result.

# time complexity is O(logk)

def square_root(k):
    left, right = 0, k

    while left <= right:
        mid = left + (right - left) // 2
        mid_square = mid * mid

        if mid_square <= k:
            left = mid + 1
        else:
            right = mid - 1

    return left - 1
