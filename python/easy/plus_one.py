def plus_one(digits):
    digits.insert(0, 0)
    n = len(digits)
    if digits[n - 1] < 9:
        digits[n - 1] += 1
    else:
        digits[n - 1] = 0
        digits[:n - 1] = plus_one(digits[1:n - 1])
    if digits[0] == 0:
        del digits[0]
    return digits

