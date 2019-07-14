# given a 2D sorted array(i.e., all rows and columns are nondecreasing),
# find wether the given value k is in the 2D array or not.

# start from the last value at row 0, do the comparison between k and
# array[0][n-1], if 
# 1). array[0][n-1] < k, eliminate row 0, go to next row
# 2). array[0][n-1] > k, eliminate column n-1, go to previous column
# 3). array[0][n-1] == k, return True
# keep doing steps above until we find the k or out of boundaries.

# time complexity is O(m + n)

def matrix_search(array, x):
    row, col = 0, len(array[0]) - 1

    while row < len(array) and col >=0:
        if array[row][col] == x:
            return True
        elif array[row][col] < x:
            row += 1
        else:
            col -= 1

    return False
