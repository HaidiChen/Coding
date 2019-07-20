# given an array, return whether it is possible or not to modify at most 1 
# value to make the array non-decreasing.

# time complexity is O(n)
# space complexity is O(1)

class Solution(object):
    def check(self, array):
        if array is None or len(array) == 0:
            return False

        counter = 0

        for i in range(1, len(array)):
            if array[i] < array[i - 1]:
                tmp = array[i - 2] if i - 2 >= 0 else float('-inf')

                if array[i] >= tmp:
                    counter += 1
                    if counter > 1:
                        return False
                else:
                    return False

        return True
