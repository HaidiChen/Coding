def ts(arr):
    n = len(arr)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    print(arr[i], arr[j], arr[k])

def ts2(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            try:
                temp = arr[:]
                del temp[j]
                del temp[i]
                k = temp.index(0 - arr[i] - arr[j])
                print(arr[i], arr[j], temp[k])
            except ValueError:
                continue

def ts3(arr):
    sa = sorted(list(set(arr)))
    n = len(sa)
    for i in range(n - 2):
        low = i + 1
        high = n - 1
        s = 0 - sa[i]
        while low < high:
            if sa[low] + sa[high] == s:
                print(sa[i], sa[low], sa[high])
                low = low + 1
                high = high - 1
            elif sa[low] + sa[high] < s:
                low = low + 1
            else:
                high = high - 1
