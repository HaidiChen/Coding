def nd(arr):
    n = len(arr)
    missing = []
    for i in range(n):
        t = ls(i + 1, arr)
        if t == False:
            missing.append(i + 1)
    print(missing)

def ls(x, arr):
    n = len(arr)
    for i in range(n):
        if arr[i] == x:
            return True
    else:
        return False

def nd2(arr):
    n = len(arr)
    for i in range(n):
        val = abs(arr[i]) - 1
        if arr[val] > 0:
            arr[val] = -arr[val]

    missing = []
    for i in range(n):
        if arr[i] > 0:
            missing.append(i + 1)
    print(missing)
