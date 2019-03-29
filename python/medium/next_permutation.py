def np(arr):
    n = len(arr)
    if n < 2:
        print(arr)
        return
    i = n - 2
    while arr[i] >= arr[i + 1] and i >= 0:
        i = i - 1
    if i < 0:
        print(sorted(arr))
        return
    else:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        arr[i + 1 : n] = sorted(arr[i + 1 : n])
        print(arr)
