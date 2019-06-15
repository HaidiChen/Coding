def peakvalley(array):
    peak = 1

    for i in range(1, len(array)):
        if peak:
            if array[i] > array[i - 1]:
                array[i - 1], array[i] = array[i], array[i - 1]

            peak = 0
        else:
            if array[i] < array[i - 1]:
                array[i - 1], array[i] = array[i], array[i - 1]

            peak = 1

def main():
    x = [4,2,1,5,3,6,9]
    peakvalley(x)
    print(x)

if __name__ == "__main__":
    main()
