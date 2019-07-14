# find the first appearance of target value k in the sorted array.
# return -1 if not exist otherwise return the index.

# the solution is adapted from the regular binary search tech.
# do not stop when you find the target k, and always take the left
# half if one target value is found.

# time complexity is O(logn)

def find_first_of_k(array, k):
    left, right = 0, len(array) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if array[mid] < k:
            left = mid + 1
        elif array[mid] == k:
            result = mid
            right = mid - 1
        else:
            right = mid - 1

    return result
