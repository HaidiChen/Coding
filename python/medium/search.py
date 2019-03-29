import math

def search(arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low  + high) // 2
        num = 0
        if (arr[mid] < arr[0]) == (target < arr[0]):
            num = arr[mid]
        elif target < arr[0]:
            num = -math.inf
        else:
            num = math.inf
        if num < target:
            low = mid + 1
        elif num > target:
            high = mid - 1
        else:
            print(mid)
            return
    else:
        print(-1)
