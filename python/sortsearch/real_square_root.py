import math
# compute the square root of a floating point value

# start with range (x, 1.0) if x(the target value) is smaller than 1.0
# else start with range(1.0, x) if x >= 1.0

# time complexity is O(log(x/s)) where s is the tolerance

def real_square_root(x):
    left, right = (x, 1.0) if x < 1.0 else (1.0, x)

    while not math.isclose(left, right):
        mid = 0.5 * (left + right)
        mid_square = mid * mid
        if mid_square > x:
            right = mid
        else:
            left = mid

    return left
