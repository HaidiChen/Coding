def rotate(array):
    N = len(array)
    for row in range(N):
        for col in range(N // 2):
            array[row][col], array[row][N - 1 - col] = array[row][N - 1 - col], array[row][col]

    for r in range(N):
        for c in range(N - r):
            array[r][c], array[N - 1 - c][N - 1 - r] = array[N - 1 - c][N - 1 - r], array[r][c]

def main():
    ex = [
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]
            ]
    rotate(ex)
    for i in ex:
        print(i)

if __name__ == '__main__':
    main()
