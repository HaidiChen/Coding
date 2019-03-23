def fd(arr):
    for x in arr:
        t = arr.count(x)
        if t > 1:
            return True
    else:
        return False

def fd2(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return True
    else:
        return False

def fd3(arr):
    temp = set(arr)
    if len(temp) != len(arr):
        return True
    else:
        return False

def fd4(arr):
    for x in arr:
        first = arr.index(x)
        try:
            second = arr.index(x, first + 1)
            return True
        except:
            continue
    else:
        return False

def fd5(arr):
    ''' sort first, then locate duplicate elements '''
    pass
