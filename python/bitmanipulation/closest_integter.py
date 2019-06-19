# find the closest integer with same weight
# weight: the number of 1s in binary representation
def closest_integer(x):
    BITS = 64
    for i in range(BITS - 1):
        # find the two rightmost consecutive bits that differ
        if (x >> i) & 1 != (x >> (i + 1)) & 1:
            x ^= (1 << i) | (1 << (i + 1))
            return x

    return ValueError('all 0 or 1')

def main():
    result = closest_integer(17)
    print(result)

if __name__ == '__main__':
    main()
