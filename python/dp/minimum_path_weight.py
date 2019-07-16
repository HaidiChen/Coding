# find the path that has the minimum weight in the following
# array and return the weight.
#    2
#   4 4
#  8 5 6
# 4 2 6 2
#1 5 2 3 4

# the solution is starting from bottom or top, here we start
# from the bottom row. from the bottom row, we could calculate
# the new weights on second last row. e.g., for the first
# element on the second last row (i.e., 4), this element is 
# updated to min(4 + 1, 4 + 5) which is 5, the next element is
# updated to min(2 + 5, 2 + 2) which is 4, etc., when we reach
# the top, we happen to have the minimum weight.

# or we can start from the top to bottom row, then when we
# reach the last row, we pick the min value in the last row as
# the result.

# the time complexity is O(n^2) where the n is the number of
# rows in this array.

class Solution:
    def minimum_path_weight(self, triangle):
        min_weight_to_curr_row = [0]

        for row in triangle:
            min_weight_to_curr_row = [row[j] + 
                    min(min_weight_to_curr_row[max(j - 1, 0)],
                        min_weight_to_curr_row[min(j, 
                            len(min_weight_to_curr_row) - 1)])
                        for j in range(len(row))]

        return min(min_weight_to_curr_row)
