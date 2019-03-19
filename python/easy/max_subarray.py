def max_subarray2(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    startOld = start = end = 0
    for i, x in enumerate(A[1:], 1):
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
        if max_ending_here < 0:
            start = i + 1
        elif max_ending_here == max_so_far:
            startOld = start
            end = i
    return (max_so_far, startOld, end)

ex = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
ex2 = [-2, 1, -3, 4, -1, 2, 1, -8, 7]

def test():
    print(max_subarray(ex))
    print(max_subarray(ex2))

def test2():
    print(max_subarray2(ex))
