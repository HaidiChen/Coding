def rearrange(array):
    lteq = True
    for i in range(len(array) - 1):
        if (lteq and array[i] > array[i + 1]) or ((not lteq) and array[i] < array[i + 1]):
            array[i], array[i + 1] = array[i + 1], array[i]
        lteq = not lteq

    print(array)

def main():
    array = [1,2,3,4,5,6,7,8,9]
    rearrange(array)

if __name__ == '__main__':
    main()
