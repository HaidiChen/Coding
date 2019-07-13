# compute the intersection of two sorted arrays
# which could have duplicates in each array and
# the output should be free of duplicates
# e.g., <1,3,3,4,6,6> and <3,3,3,6,9> should 
# return <3,6>

# this solution uses the two pointers strategy
# which achieves O(m + n) time complexity where
# m and n are lengths of array A and array B.

def intersect_two_sorted_arrays(A, B):
    i, j, result = 0, 0, set()

    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            # since we use set to store the result
            # it automatically discard duplicates
            result.add(A[i])
            i += 1
            j += 1
        elif A[i] > B[j]:
            j += 1
        else:
            i += 1

    return result
