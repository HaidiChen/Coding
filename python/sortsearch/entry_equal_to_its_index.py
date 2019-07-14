# find a value in a sorted array such that the value is equal to its
# index. Assume that all elements are distinct.

# the solution is similar to regular binary search. if array[i] > i,
# then all subsequent values is larger than their indices as all elements
# are distinct. Similar, if array[i] < i, all previous elements will
# be smaller than their indices.

# time complexity is O(logn)

def search_entry_equal_to_its_index(array):
    left, right = 0, len(array) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if array[mid] == mid:
            result = mid
            break
        elif array[mid] > mid:
            right = mid - 1
        else:
            left = mid + 1

    return result
