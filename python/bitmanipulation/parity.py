# compute the parity of a large number of 64-bit word
# parity is 1 if number of bits that are set to 1 is odd,
# otherwise it is 0

# 1). brute-force way, time  complexity O(n) where n is 
# the number of bits of this integer
def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1

    return result

# 2). improved approach, time complexity O(k) where k is
# the number of bits that are set to 1 in this integer
def parity2(x):
    result = 0
    while x:
        result ^= 1
        x &= (x - 1)    # erase the lowest set bit

    return result

# 3). optimus approach, time complexity O(log n) where n
# is the word size
def parity3(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1
