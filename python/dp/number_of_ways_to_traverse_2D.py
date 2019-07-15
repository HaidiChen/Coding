# compute the number of ways traversing a 2D array by starting
# from the top left corner and ending at the bottom right corner.
# assume that you can only go right or down.

# the number of ways to get to array[m][n] is the number of ways
# to get to array[m][n-1] plus the number of ways to get to
# array[m-1][n]. so the array[m][n] = array[m-1][n] + array[m][n-1]

# time complexity is O(n) where n is the total number of elements
# in this 2D array

def number_of_ways(array):

    def compute_ways(row, column):
        if row < 0 or column < 0:
            return 0
        return array[row][column]

    array[0][0] = 1

    for row in range(len(array)):
        for col in range(len(array[0])):
            if row == 0 and col == 0:
                continue
            array[row][col] = compute_ways(row, col - 1) + (
                    compute_ways(row - 1, col))

    m = len(array) - 1
    n = len(array[0]) - 1
    return array[m][n]


# this solution is provided by EPI, it uses recursion to solve the 
# problem, but the idea behind it is the same as the above one.

def number_of_ways2(n, m):
    def compute_number_of_ways_to_xy(x, y):
        if x == y == 0:
            return 1
        if number_of_ways[x][y] == 0:
            ways_top = 0 if x == 0 else compute_number_of_ways_to_xy(x - 1, y)
            ways_left = 0 if y == 0 else compute_number_of_ways_to_xy(x, y - 1)
            number_of_ways[x][y] = ways_top + ways_left

        return number_of_ways[x][y]

    number_of_ways = [[0] * m for _ in range(n)]

    return compute_number_of_ways_to_xy(n - 1, m - 1)
