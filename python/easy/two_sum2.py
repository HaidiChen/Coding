def ts(arr, target):
    n = len(arr)
    for i in range(n):
        r = search(target - arr[i], arr[i + 1 : n])
        if r != -1:
            return print('first index: {0}, second index: {1}'.format(i, (i + 1 + r)))
    print('nothing')

def search(x, arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def ts2(arr, target):
    n = len(arr)
    for i in range(n):
        try:
            s = arr.index(target - arr[i])
            print('first index: {0}, second index: {1}'.format(i, s))
            break
        except ValueError:
            print('nothing')

def ts3(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        value = arr[left] + arr[right]
        if value == target:
            print('first index: {0}, second index: {1}'.format(left, right))
            break
        elif value > target:
            right = right - 1
        else:
            left = left + 1
    else:
        print('nothing')
