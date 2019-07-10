def k_bit_flip(array, K):

    if array is None or len(array) < 1 or len(array) > 30000:
        return -1
    if K < 1 or K > len(array):
        return -1

    result = 0

    def true_flip(array):
        if len(array) < K:
            for e in array:
                if e == 0:
                    return False
            return True

        for i in range(K):
            if array[i] == 0:
                flip(K, array, i)
                return true_flip(array[i:])

        return true_flip(array[K:])

    def flip(length, array, offset):
        nonlocal result
        result += 1
        for i in range(offset, offset + K):
            array[i] = array[i] ^ 1

    if true_flip(array):
        return result
    return -1
