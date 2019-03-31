def sr(arr, target):
    first = find_first(arr, target)
    last = find_last(arr, target)
    print([first, last])

def find_first(arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if (mid == 0 or arr[mid - 1] < target) and arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    else:
        return -1

def find_last(arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    while low <= high:
        mid = (high + low) // 2
        if (mid == n - 1 or arr[mid + 1] > target) and arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    else:
        return -1
