def mz(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] == 0:
            j = i
            while (j < n - 1):
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                j = j + 1
        else:
            continue
    print(arr)

def mz2(arr):
    n = len(arr)
    while (arr.count(0) > 0):
        arr.remove(0)
    while (len(arr) < n):
        arr.append(0)
    print(arr)

def mz3(arr):
    n = len(arr)
    i = 0
    for x in arr:
        if x != 0:
            arr[i] = x
            i = i + 1
    while (i < n):
        arr[i] = 0
        i = i + 1
    print(arr)
