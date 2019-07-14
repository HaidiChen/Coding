# find the smallest value in a cyclically sorted array
# and return the index

# if the middle value is larger than the rightmost one,
# it indicates that the smallest value will appear in
# the right half; if the middle value is less than the
# rightmost one, then the smallest value appears in the
# left half.

# time complexity is O(logn)

def search_smallest(array):
    left, right = 0, len(array) - 1

    while left < right:
        mid = left + (right - left) // 2
        if array[mid] > array[right]:
            left = mid + 1
        else:
            right = mid

    return left
