def tm(arr):
    if len(arr) == 1:
        print(arr[0])
        return
    elif len(arr) == 2:
        print(max(arr[0], arr[1]))
        return
    else:
        temp = list(set(arr))
        i = 0
        while (i < 3):
            max_num = findmax(temp)
            temp.remove(max_num)
            i = i + 1
        print(max_num)
        return

def findmax(arr):
    m = arr[0]
    n = len(arr)
    for i in range(1, n):
        if arr[i] > m:
            m = arr[i]
    return m

def tm2(arr):
    if len(arr) == 1:
        print(arr[0])
        return
    elif len(arr) == 2:
        print(max(arr))
        return
    else:
        temp = set(arr)
        for i in range(3):
            m = max(temp)
            temp.remove(m)
        print(m)