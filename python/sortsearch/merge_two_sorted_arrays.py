# given two sorted arrays A and B, merge them
# into A, assume that A has enough empty space
# at the end to hold all elements of B

# if we start from the begining of the two arrays,
# we need to face the shifting operation which is
# expensive.
# so, instead of starting from the begining, we
# can iterate from the end of two arrays and put
# the largest one at the correct place.

# time complexity is O(m + n) where m and n are
# true lengths of A and B

def merge_two_sorted_arrays(A, m, B, n):
    i, j = m - 1, n - 1
    last_idx = m + n - 1

    while i >= 0 and j >= 0:
        if A[i] > B[j]:
            A[last_idx] = A[i]
            i -= 1
        else:
            A[last_idx] = B[j]
            j -= 1

        last_idx -= 1

    while j >= 0:
        A[last_idx] = B[j]
        j -= 1
        last_idx -= 1
