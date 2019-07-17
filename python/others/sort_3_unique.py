# given an array which has only 3 unique numbers (1,2,3)
# sort the array in O(n) time

# the solution is:
# 1) we can count the number of 1, 2, and 3 and rebuild
# a new array from 1 to 3 using the numbers we get.
# 2) we can do this in place by swapping 1 to the leftmost
# place and swapping 3 to the rightmost place. pay attention
# to swapping the 3 here. if you are swappring two 3s. e.g.,
# if array is [3,1,2,3], then you are going to swap the index
# 0 and index 3 as the first element is 3. But after the swap,
# we can see that the first element is still 3, so we need to
# keep the index at 0 to swap it again.

# the space complexity is O(1)

class Solution:
    def sort_with_new_list(self, array):
        count1, count2, count3 = 0, 0, 0

        for n in array:
            if n == 1:
                count1 += 1
            elif n == 2:
                count2 += 1
            elif n == 3:
                count3 += 1

        return [1] * count1 + [2] * count2 + [3] * count3

    def sort_in_place(self, array):
        index_one = 0
        index_three = len(array) - 1

        # index of the element we are looking at
        i = 0
        while i <= index_three:
            if array[i] == 1:
                array[i], array[index_one] = (array[index_one],
                        array[i])
                index_one += 1
                i += 1
            elif array[i] == 3:
                array[i], array[index_three] = (array[index_three],
                        array[i])
                # only change the rightmost index
                # leave the index i stay still
                index_three -= 1
            else:
                i += 1
