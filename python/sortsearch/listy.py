def searchListy(array, target):
    left = 0
    right = 16
    while left <= right:
        mid = left + (right - left) // 2

        try:
            if array[mid] < target:
                left = mid + 1
                if left == right:
                    right *= 2
            elif array[mid] > target:
                right -= 1
            else:
                return mid

        except IndexError:
            right = mid - 1

    return -1
