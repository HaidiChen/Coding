# compute a gray code

# this solution compute one distinct value at a time
# e.g., for 2 bit gray code, it goes like following:
# start with 00 -> 01 -> 11(notice that 00 already exists, so we skip that) -> 10 end
# so the 2 bit gray code is [0,1,3,2]
#
# e.g., for 3 bit gray code, it goes like following:
# start with 000 -> 001 -> 011(000 already exists) -> 010 -> 110(011, 000 already exist)
# -> 111 -> 101(110 already exists) -> 100 end
# so the 3 bit gray code is [0,1,3,2,6,7,5,4]

def gray_code(num_bits):
    def directed_gray_code(history):
        def differs_by_one_bit(x, y):
            bit_difference = x ^ y
            return bit_difference and not (bit_difference & (bit_difference - 1))

        if len(result) == 1 << num_bits:
            return differs_by_one_bit(result[0], result[-1])

        for i in range(num_bits):
            previous_code = result[-1]
            candidate_next_code = previous_code ^ (1 << i)
            if candidate_next_code not in history:
                history.add(candidate_next_code)
                result.append(candidate_next_code)
                if directed_gray_code(history):
                    return True
                history.remove(candidate_next_code)
                del result[-1]

        return False

    result = [0]
    directed_gray_code(set([0]))
    return result


# alternative solution
# n bit gray code is n-1 bit gray code plus reversed n-1 bit gray code prepended with 1
# e.g., a 2 bit gray code is [0,1,3,2] which is [00, 01, 11, 10] whose reversed form is 
# [10, 11, 01, 00], we prepend 0 to the original gray code and prepend 1 to the reversed,
# then the 3 bit gray code will be [000, 001, 011, 010] + [110, 111, 101, 100]
# which is [000, 001, 011, 010, 110, 111, 101, 100] which is [0,1,3,2,6,7,5,4]

def gray_code_alt(num_bits):
    if num_bits == 0:
        return [0]

    gray_code_num_bits_minus_1 = gray_code_alt(num_bits - 1)
    leading_bit_one = 1 << (num_bits - 1)
    return gray_code_num_bits_minus_1 + [leading_bit_one | i for i in reversed(gray_code_num_bits_minus_1)]

def main():
    result = gray_code(3)
    result2 = gray_code_alt(3)
    print(result)
    print(result2)

if __name__ == '__main__':
    main()
