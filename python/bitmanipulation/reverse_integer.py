# reverse an integer
# e.g., 345 -> 543, -142 -> -241

def reverse_int(x):
    result = 0
    remaining_x = abs(x)

    while remaining_x:
        result = result * 10 + remaining_x % 10
        remaining_x = remaining_x // 10

    return -result if x < 0 else result
