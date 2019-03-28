def np(arr):
    n = len(arr)
    i = n - 2
    while arr[i] >= arr[i + 1]:
        i = i - 1
    arr[i], arr[i + 1] = arr[i + 1], arr[i]
    arr[i + 1 : n] = sorted(arr[i + 1 : n])
    print(arr)
