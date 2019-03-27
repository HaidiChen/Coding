def fs(arr, target):
    n = len(arr)
    res = []
    if n < 4:
        return res
    arr.sort()
    m = arr[n - 1]
    if 4 * arr[0] > target or 4 * m < target:
        return res
    for i in range(n):
        z = arr[i]
        if i > 0 and z == arr[i - 1]:
            continue
        if z + 3 * m < target:
            continue
        if 4 * z > target:
            break
        if 4 * z == target:
            if i + 3 < n and arr[i + 3] == z:
                res.append([z,z,z,z])
            break

        ths(arr, target - z, i + 1, n - 1, res, z)
    print(res)

def ths(arr, target, low, high, res, z1):
    if low + 1 >= high:
        return
    m = arr[high]
    if 3 * arr[low] > target or 3 * m < target:
        return
    for i in range(low, high - 1):
        z = arr[i]
        if i > low and z == arr[i - 1]:
            continue
        if z + 2 * m < target:
            continue
        if 3 * z > target:
            break
        if 3 * z == target:
            if i + 1 < high and arr[i + 2] == z:
                res.append([z1,z,z,z])
            break
        tws(arr, target - z, i + 1, high, res, z1, z)

def tws(arr, target, low, high, res, z1, z2):
    if low >= high:
        return
    if 2 * arr[low] > target or 2 * arr[high] < target:
        return
    i = low
    j = high
    while i < j:
        s = arr[i] + arr[j]
        if s == target:
            res.append([z1, z2, arr[i], arr[j]])
            x = arr[i]
            i = i + 1
            while i < j:
                if x == arr[i]:
                    i = i + 1
                else:
                    break
            x = arr[j]
            j = j - 1
            while i < j:
                if x == arr[j]:
                    j = j - 1
                else:
                    break
        elif s < target:
            i = i + 1
        else:
            j = j - 1
