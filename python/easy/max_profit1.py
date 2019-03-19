def maxprofit(arr):
    n = len(arr)
    mp = 0
    for j in range(n - 1):
        for i in range(j + 1, n):
            mp = max(mp, arr[i] - arr[j])
    print(mp)

def mp(arr):
    n = len(arr)
    maxc = maxs = 0
    for i in range(1, n):
        maxc = maxc + (arr[i] - arr[i - 1])
        maxc = max(maxc, 0)
        maxs = max(maxc, maxs)
    print(maxs)
