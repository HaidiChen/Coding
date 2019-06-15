def rotateBinary(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = left + (right - left) // 2
        #midvalue = array[mid]
        if not (target < array[0]) == (array[mid] < array[0]):
            if target < array[0]:
                array[mid] = -9999
            else:
                array[mid] = 9999
        if target > array[mid]:
            left = mid + 1
        elif target < array[mid]:
            right = mid - 1 
        else:
            return mid

    return -1

