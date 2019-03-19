def mp(arr):
    maxc = maxs = 0
    total = 0
    n = len(arr)
    for i in range(1, n):
        maxc_temp = maxc + (arr[i] - arr[i - 1])
        if maxc_temp < maxc:
            total = total + maxs
            maxs = 0
            maxc = 0
        else:
            maxc = maxc_temp
            maxs = max(maxc, maxs)
    total = total + maxs
    print(total)

def mp2(arr):
    total = 0
    n = len(arr)
    for i in range(n - 1):
        if arr[i + 1] > arr[i]:
            total = total + arr[i + 1] - arr[i]
    print(total)
