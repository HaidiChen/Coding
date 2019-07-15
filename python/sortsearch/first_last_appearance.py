# find the first and last indices of the target value in a
# sorted array, if not exist, return -1.

# adapt binary search to find the first and last indices 
# individually.

# time complexity is O(logn)

def find_appearance(array, target):
    def find_target(target, is_first):
        left = 0
        right = len(array) - 1
        result = -1

        while left <= right:
            mid = left + (right - left) // 2
            if array[mid] == target:
                result = mid
                if is_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif array[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return result

    start = find_target(target, True)
    end = find_target(target, False)

    return [start, end]


# this solution is provided by dailyinterviewpro.
# and it uses recursion instead of iteration so there
# is some stack space usage here.

class Solution:
    def get_range(self, arr, target):
        low = 0
        high = len(arr) - 1
        first = self.firstIndex(arr, low, high, target)
        last = self.lastIndex(arr, low, high, target)
        return [first, last]

    def firstIndex(self, arr, low, high, target):
        if (high >= low):
            mid = low + (high - low) // 2
            if ((mid == 0 or target > arr[mid - 1]) and arr[mid] == target):
                return mid
            elif (target > arr[mid]):
                return self.firstIndex(arr, mid + 1, high, target)
            else:
                return self.firstIndex(arr, low, mid - 1, target)

        return -1

    def lastIndex(self, arr, low, high, target):
        if (high >= low):
            mid = low + (high - low) // 2
            if ((mid == len(arr) - 1 or target < arr[mid + 1]) and arr[mid] == target):
                return mid
            elif arr[mid] > target:
                return self.lastIndex(arr, low, mid - 1, target)
            else:
                return self.lastIndex(arr, mid + 1, high, target)

        return -1
