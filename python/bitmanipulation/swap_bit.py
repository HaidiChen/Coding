# swap the ith bit and jth bit
def swap_bit(x, i, j):

    # swap only happens when ith and jth bit are different
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask

    return x

def main():
    result = swap_bit(13, 2, 6)
    print(result)

if __name__ == '__main__':
    main()
