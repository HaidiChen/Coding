def mn(arr):
    n = len(arr)
    for i in range(n):
        if i != arr[i]:
            return i
    return -1
