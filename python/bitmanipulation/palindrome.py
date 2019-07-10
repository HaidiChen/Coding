import math
# check if an integer is a palindrome or not

def is_palindrome(x):
    if x <= 0:
        return x == 0

    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10 ** (num_digits - 1)

    for _ in range(num_digits // 2):
        msd = x // msd_mask
        lsd = x % 10
        if msd != lsd:
            return False
        x = x % msd_mask
        x = x // 10
        msd_mask = msd_mask // 100

    return True

# alternatively, we can reverse the integer to check
# if it is the same as the previous one

def is_palindrome2(x):
    if x <= 0:
        return x == 0

    rev_int = 0
    remaining_x = x

    while remaining_x:
        rev_int = rev_int * 10 + remaining_x % 10
        remaining_x //= 10

    return rev_int == x
