from merge_sorted_arrays import *
# sort a k increasing decreasing array

# the solution here split the array to k sorted subarrays
# if the subarray is in a decreasing order, reverse it
# and then merge the k sorted arrays using the solution
# of merge_sorted_arrays
# time complexity is O(nlogk) where n is the length of the
# input array
# space complexity is O(n)

def sort_k_increasing_decreasing_array(array):
    # decompose the array into a set of sorted subarrays
    sorted_subarrays = []
    INCREASING, DECREASING = range(2)
    subarray_type = INCREASING
    start_idx = 0

    for i in range(1, len(array) + 1):
        if (i == len(array) or (array[i - 1] < array[i]
            and subarray_type == DECREASING) or 
            (array[i - 1] > array[i] and subarray_type == INCREASING)):
            sorted_subarrays.append(array[start_idx:i] if subarray_type ==
                    INCREASING else array[i - 1:start_idx - 1: -1])
            start_idx = i
            subarray_type = (INCREASING if subarray_type == DECREASING 
                    else DECREASING)

    return merge_sorted_arrays(sorted_subarrays)
