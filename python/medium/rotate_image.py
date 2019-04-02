def rotate(arr):
    n = len(arr)
    for r in range(n):
        for c in range(r, n):
            arr[c][r], arr[r][c] = arr[r][c], arr[c][r]
    for r in range(n):
        for c in range(n // 2):
            arr[r][n - 1 -c], arr[r][c] = arr[r][c], arr[r][n - 1 - c]
    for i in arr:
        print(i)
