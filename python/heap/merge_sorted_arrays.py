import heapq

# merge several (at least two) arrays into one
# this approach uses min-heap to keep track the
# smallest entry from each of the sorted array
# time complexity = O(nlogk) where n is the total
# number existed in these sorted arrays and k is
# the number of sorted arrays
# space complexity is O(k) 

def merge_sorted_arrays(sorted_arrays):
    min_heap = []

    # get the iterators for each array
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]

    # put the first element of each array into the min-heap
    for i, it in enumerate(sorted_arrays_iters):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    result = []
    while min_heap:
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        smallest_array_iter = sorted_arrays_iters[smallest_array_i]
        result.append(smallest_entry)
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_i))

    return result
