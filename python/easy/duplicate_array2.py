def fd(arr, k=1):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                if (j - i) <= k:
                    return True
    return False

def fd2(arr, k = 1):
    for x in arr:
        first = arr.index(x)
        try:
            second = arr.index(x, first + 1)
            if (second - first) <= k:
                return True
        except:
            continue
    else:
        return False
