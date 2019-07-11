import itertools
import heapq
# sort the almost sorted array
# this kind of array ensures that every element
# is at most k away from its final sorted place

# this solution has the following idea
# when we are looking at (k + 1)th element, we
# know that the smallest element in ths (k + 1)
# elements subarray should be put at the begining
# of this subarray, why? Because the smallest one
# is k away from its final sorted place, so the 
# furthest place where the smallest element is put
# is going to be the (k + 1)th place.

# so we store the k + 1 elements at a time and
# extract the minimum element followed by adding
# another element to keep the number of elements
# as k + 1. To efficiently extract the min element,
# we use min-heap

# time complexity is O(nlogk)
# space complexity is O(k)

def sort_almost_sorted_array(array, k):
    result = []
    min_heap = []

    # put the first k elements into the min_heap
    for x in array[:k]:
        heapq.heappush(min_heap, x)

    # add the new element to min_heap and extract
    # the smallest one
    for x in array[k:]:
        smallest = heapq.heappushpop(min_heap, x)
        result.append(smallest)

    # if we have elements left in heap, extract
    # the smallest one by one
    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)

    return result
